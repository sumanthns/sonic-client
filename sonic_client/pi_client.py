import RPi.GPIO as GPIO

class PiClient(object):
    def output(self, led, value):
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, value)
