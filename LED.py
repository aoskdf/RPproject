import RPi.GPIO as GPIO
# time
import time
GPIO.setmode (GPIO.
LED = 11
GPIO.setup (LED, GPIO.OUT, initial=GPIO.
GPIO.output (LED, GPIO.
time.sleep(10)
