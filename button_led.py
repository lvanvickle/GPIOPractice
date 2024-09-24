import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
# Set up component pins
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as output pin for LED
GPIO.setup(13, GPIO.IN) # Set up GPIO13 as input pin for button

try:
    while True:
        if(GPIO.input(13)):
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
except KeyboardInterrupt:
    pass

# Clean up GPIO settings before exiting
GPIO.cleanup()
