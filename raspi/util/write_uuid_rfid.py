import uuid

from pirc522 import RFID

def main():
    id = uuid.uuid4()
    key_a = (0x01, 0x02, 0x03, 0x04, 0x05, 0x06)
    block_addr = 8
    write_uuid(id, key_a, block_addr)


def write_uuid(id, key_a, block_addr):
    rdr = RFID()
    util = rdr.util() 
    util.debug = true

    rdr.wait_for_tag()

    (error, data) = rdr.request()

    if error:
        raise Exception('Request error.')

    (error, uid) = rdr.anticoll()

    if error:
        raise Exception('Anticoll error.')

    print('Card UID: {}'.format(''.join(hex(x) for x in uid))))

    util.set_tag(uid)

    uid_bytes = bytearray.fromhex(id.hex)

    util.auth(rdr.auth_a, key_a)
    util.rewrite(block_address = block_addr, new_bytes = uid_bytes)

    util.deauth()
    rdr.cleanup()


if __name__ == '__main__':
    main()
