from raspi.lcd import LCD
from raspi.rfid import RFID
from event_bus import EventBus
from raspi import config
from enum import Enum

class State(Enum):
    AUTHENTICATE = 1
    AUTHORIZE = 2
    ALCOHOL_LEVEL = 3
    RESULT = 4

bus = EventBus()

lcd = LCD()
rfid = RFID(bus)

state = State.AUTHENTICATE


@bus.on(config.RFID_READ_EVENT)
def rfid_read_event(uid):
    global state
    if state == State.AUTHENTICATE:
        state = State.AUTHORIZE
        lcd.setRGB(77, 182, 172)
        lcd.setText('Checking authorization')


if __name__ == "__main__":
    lcd.setRGB(255, 238, 88)
    lcd.setText('Pass your RFID card')

    rfid.listen()
