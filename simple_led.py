import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as an output pin

# Turn the LED on
GPIO.output(18, GPIO.HIGH)

# Keep the LED on
try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	pass

# Clean up GPIO settings before exiting
GPIO.cleanup()
