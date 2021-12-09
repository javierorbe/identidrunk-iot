from grove.adc import ADC


class AlcoholSensor:
    # Channel can be 0 or 1 -> A0 or A1
    def __init__(self, channel=0):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        return self.adc.read(self.channel)
