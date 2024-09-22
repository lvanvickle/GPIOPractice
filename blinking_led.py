import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as an output pin

# Turn the LED on and off
try:
	while True:
		GPIO.output(18, GPIO.HIGH) # Turn the LED on
		time.sleep(1) # Wait
		GPIO.output(18, GPIO.LOW) # Turn the LED off
		time.sleep(1) # Wait
except KeyboardInterrupt:
	pass

# Clean up GPIO settings before exiting
GPIO.cleanup()
