import uuid

from pirc522 import RFID as RC522

import config


class RFID:
    def __init__(self, bus) -> None:
        self._bus = bus
        self._rdr = RC522()


    def listen(self):
        util = self._rdr.util()
        while True:
            # Wait for tag
            self._rdr.wait_for_tag()
            # Request tag
            (error, data) = self._rdr.request()
            if not error:
                (error, uid) = self._rdr.anticoll()
                if not error:
                    print('Card UID: {}'.format(' '.join(hex(x) for x in uid)))

                    util.set_tag(uid)
                    util.auth(self._rdr.auth_a, config.RFID_UUID_KEY_A)

                    (error, data) = self._rdr.read(config.RFID_UUID_BLOCK_ADDR)

                    if not error:
                        id = ''.join('{:02x}'.format(x) for x in data)
                        self._bus.emit(config.RFID_READ_EVENT, uuid.UUID(id))

                    util.deauth()
