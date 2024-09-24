import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as an output pin
GPIO.setup(12, GPIO.OUT) # Set GPIO12 as an output pin
GPIO.setup(17, GPIO.OUT) # Set GPIO17 as an output pin
GPIO.setup(6, GPIO.OUT) # Set GPIO6 as an output pin

# Ensure all LEDs are turned off
GPIO.output(18, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

# Turn LEDs on one at a time
try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(6, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up GPIO settings before exiting
GPIO.cleanup()