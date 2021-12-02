import math
import sys
import time
from grove.adc import ADC


class AlcoholSensor:

    def __init__(self, channel):
        # Channel can be 0 or 1 -> A0 or A1
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        value = self.adc.read(self.channel)
        return value


def main():
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = AlcoholSensor(int(sys.argv[1]))

    print('Detecting...')
    while True:
        sensor_value = sensor.value
        sensor_volt = sensor_value / 1024 * 5.0
        rs_gas = sensor_volt / 5.0 - sensor_volt
        print('Gas value: {0}'.format(rs_gas))
        time.sleep(.5)

if __name__ == '__main__':
    main()
