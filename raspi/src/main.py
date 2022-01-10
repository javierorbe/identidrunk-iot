import requests
import time
from enum import Enum

from event_bus import EventBus

import config
from lcd import LCD
from rfid import RFID
from alcohol_sensor import AlcoholSensor


class State(Enum):
    AUTHENTICATE = 1
    AUTHORIZE = 2
    ALCOHOL_LEVEL = 3
    RESULT = 4
    ERROR = 5

bus = EventBus()

lcd = LCD()
rfid = RFID(bus)
alcohol_sensor = AlcoholSensor(channel=0)

state = State.AUTHENTICATE

@bus.on(config.RFID_READ_EVENT)
def rfid_read_event(uid):
    global state
    if state != State.AUTHENTICATE:
        return

    state = State.AUTHORIZE
    lcd.setRGB(77, 182, 172)
    lcd.setText('Checking authorization')
    response = requests.get(config.AUTH_RESOURCE, params={ 'uid': str(uid) })
    time.sleep(0.5)
    if response.status_code == requests.codes.ok:
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Blow to the breathalyzer')

        state = State.ALCOHOL_LEVEL
        alcohol_val = read_max_alcohol_value()
        evaluate_result(uid, alcohol_val)

        time.sleep(2)
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Pass your RFID card')
        state = State.AUTHENTICATE
    else:
        state = State.ERROR
        lcd.setRGB(**config.RED)
        lcd.setText('Authorization error')
        time.sleep(2)
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Pass your RFID card')
        state = State.AUTHENTICATE


def read_max_alcohol_value():
    max_val = config.ALCOHOL_SENSOR_MAX_VAL
    t_end = time.time() + 5
    while time.time() < t_end:
        val = alcohol_sensor.value
        if val > max_val:
            max_val = val
    return max_val


def evaluate_result(uid, alcohol_level):
    global state

    if alcohol_level <= config.MAX_ALCOHOL_LEVEL:
        lcd.setRGB(**config.GREEN)
        lcd.setText('Verification completed')
    else:
        lcd.setRGB(**config.RED)
        lcd.setText('Exceed alcohol limit')

    requests.post(config.RESULT_RESOURCE, post={
        'uid': str(uid),
        'alcoholLevel': alcohol_level
    })


if __name__ == "__main__":
    lcd.setRGB(**config.YELLOW)
    lcd.setText('Pass your RFID card')
    rfid.listen()
