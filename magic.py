import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup((11,7), GPIO.OUT, initial=GPIO.LOW)
GPIO.output(11, GPIO.HIGH)
time.sleep(2)
GPIO.output(11, GPIO.LOW)
time.sleep(2)
GPIO.output(11, GPIO.HIGH)
time.sleep(2)
GPIO.cleanup()