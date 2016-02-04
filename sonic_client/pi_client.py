import RPi.GPIO as GPIO

class PiClient(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def output(self, led, value):
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, value)

    def input(self, led):
        return GPIO.input(led)
