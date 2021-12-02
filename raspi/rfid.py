from pirc522 import RFID as RC522
from raspi import config

class RFID:
    def __init__(self, bus) -> None:
        self._bus = bus
        self._rdr = RC522()

    def listen(self):
        while True:
            # Wait for tag
            self._rdr.wait_for_tag()
            # Request tag
            (error, data) = self._rdr.request()
            if not error:
                (error, uid) = self._rdr.anticoll()
                if not error:
                    self._bus.emit(config.RFID_READ_EVENT, uid)
