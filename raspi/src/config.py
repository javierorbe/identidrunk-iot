RFID_READ_EVENT = 'rfid_read'
ALCOHOL_READ_EVENT = 'alcohol_read'

ENDPOINT = 'https://'
AUTH_RESOURCE = ENDPOINT + '/api/auth'
RESULT_RESOURCE = ENDPOINT + '/api/alcohol'

YELLOW = {'r': 255, 'g': 238, 'b': 88}
RED = {'r': 239, 'g': 83, 'b': 80}
GREEN = {'r': 165, 'g': 214, 'b': 167}

ALCOHOL_SENSOR_MAX_VAL = 100000
MAX_ALCOHOL_LEVEL = 250

RFID_UUID_BLOCK_ADDR = 8
RFID_UUID_KEY_A = (0x01, 0x02, 0x03, 0x04, 0x05, 0x06)
