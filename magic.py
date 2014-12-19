import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
time.sleep(2)
GPIO.output(11, GPIO.LOW)
time.sleep(2)
GPIO.cleanup()