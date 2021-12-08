import requests
import time
from enum import Enum

from event_bus import EventBus

from raspi import config
from raspi.lcd import LCD
from raspi.rfid import RFID


class State(Enum):
    AUTHENTICATE = 1
    AUTHORIZE = 2
    ALCOHOL_LEVEL = 3
    RESULT = 4
    ERROR = 5

bus = EventBus()

lcd = LCD()
rfid = RFID(bus)

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
    response = requests.get(config.AUTH_RESOURCE, params={ uid: 12345 })
    if response.status_code == requests.codes.ok:
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Blow to the breathalyzer')
        currentUid = uid
        state = State.ALCOHOL_LEVEL
    else:
        state = State.ERROR
        lcd.setRGB(**config.RED)
        lcd.setText('Authorization error')
        time.sleep(2)
        lcd.setRGB(**config.YELLOW)
        lcd.setText('Pass your RFID card')
        state = State.AUTHENTICATE


@bus.on(config.ALCOHOL_RED_EVENT)
def alcohol_read_event(alcohol_level):
    global state
    if state != State.ALCOHOL_LEVEL:
        return
    
    if alcohol_level > config.MAX_ALCOHOL_LEVEL:
        lcd.setRGB(**config.GREEN)
        lcd.setText('Verification completed')
    else:
        lcd.setRGB(**config.RED)
        lcd.setText('Exceed alcohol limit')

    requests.post(config.RESULT_RESOURCE, data={
        uid: currentUid,
        alcoholLevel: alcohol_level
    })
    time.sleep(2)
    lcd.setRGB(**config.YELLOW)
    lcd.setText('Pass your RFID card')
    state = State.AUTHENTICATE


if __name__ == "__main__":
    lcd.setRGB(**config.YELLOW)
    lcd.setText('Pass your RFID card')

    rfid.listen()
