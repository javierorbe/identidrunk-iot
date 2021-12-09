import requests
import time
from enum import Enum

from event_bus import EventBus

from raspi import config
from raspi.lcd import LCD
from raspi.rfid import RFID
from raspi.alcohol_sensor import AlcoholSensor


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
currentUid = None

@bus.on(config.RFID_READ_EVENT)
def rfid_read_event(uid):
    global state
    if state != State.AUTHENTICATE:
        return

    state = State.AUTHORIZE
    lcd.setRGB(77, 182, 172)
    lcd.setText('Checking authorization')
    response = requests.get(config.AUTH_RESOURCE, params={ 'uid': 12345 })
    if response.status_code == requests.codes.ok:
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Blow to the breathalyzer')
        min_alcohol_val = read_min_alcohol_value()
        evaluate_result(uid, min_alcohol_val)
        state = State.ALCOHOL_LEVEL
    else:
        state = State.ERROR
        lcd.setRGB(**config.RED)
        lcd.setText('Authorization error')
        time.sleep(2)
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Pass your RFID card')
        state = State.AUTHENTICATE


def read_min_alcohol_value():
    min_val = config.ALCOHOL_SENSOR_MIN_VAL
    t_end = time.time() + 5
    while time.time() < t_end:
        val = alcohol_sensor.value
        if val < min_val:
            min_val = val
    return min_val


def evaluate_result(uid, alcohol_level):
    global state

    if alcohol_level < config.MAX_ALCOHOL_LEVEL:
        lcd.setRGB(**config.GREEN)
        lcd.setText('Verification completed')
    else:
        lcd.setRGB(**config.RED)
        lcd.setText('Exceed alcohol limit')

    requests.post(config.RESULT_RESOURCE, data={
        'uid': currentUid,
        'alcoholLevel': alcohol_level
    })
    time.sleep(2)
    lcd.setRGB(**config.YELLOW)
    lcd.setText('Pass your RFID card')
    state = State.AUTHENTICATE


if __name__ == "__main__":
    lcd.setRGB(**config.YELLOW)
    lcd.setText('Pass your RFID card')
    rfid.listen()
