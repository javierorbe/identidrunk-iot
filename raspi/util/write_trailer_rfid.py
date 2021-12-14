from pirc522 import RFID


def main():
    sector = 2
    key_a = (0xFF,) * 6
    new_key_a = (0x01, 0x02, 0x03, 0x04, 0x05, 0x06)
    new_key_b = (0x01, 0x02, 0x03, 0x04, 0x05, 0x06)
    change_key(sector, key_a, new_key_a, new_key_b)


def change_key(sector, key_a, new_key_a, new_key_b, auth_bits=(0xFF, 0x07, 0x80), user_data=0xFF):
    rdr = RFID()
    util = rdr.util() 
    util.debug = True

    rdr.wait_for_tag()

    (error, data) = rdr.request()

    if error:
        raise Exception('Request error.')

    (error, uid) = rdr.anticoll()

    if error:
        raise Exception('Anticoll error.')

    print('Card UID: {}'.format(''.join(hex(x) for x in uid))))

    util.set_tag(uid)

    util.auth(rdr.auth_a, key_a)
    
    util.write_trailer(
        sector=sector,
        key_a=new_key_a,
        auth_bits=auth_bits,
        user_data=user_data,
        key_b=new_key_b
    )

    util.deauth()
    rdr.cleanup()


if __name__ == '__main__':
    main()
