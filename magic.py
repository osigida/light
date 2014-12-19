__author__ = 'osigida'
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)


chan_list = (11)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(11, GPIO.LOW) # all LOW
time.sleep(2)
GPIO.output(11, GPIO.HIGH) # all LOW
time.sleep(2)
GPIO.output(11, GPIO.LOW) # all LOW
time.sleep(2)

GPIO.cleanup()

# time.sleep(2)
# GPIO.setup(12, GPIO.OUT)
# GPIO.output(12, 1)
# time.sleep(2)
# GPIO.cleanup()
# exit (0)
# #GPIO.output(11, GPIO.HIGH) # all LOW
# #GPIO.output(40, GPIO.HIGH)  # first LOW, second HIGH
# time.sleep(2)
# #exit (0)
# #GPIO.output(38, GPIO.HIGH)  # first LOW, second HIGH
# #GPIO.output(40, GPIO.LOW)
# GPIO.cleanup()
