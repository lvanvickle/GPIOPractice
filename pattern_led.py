import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# Set up component pins
led1= 18
led2 = 17
led3 = 12
led4 = 6
button = 13

# Set up each pin as output or input
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set up button pin as input with pull-down resistor

# Ensure LEDs start off
GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)
GPIO.output(led4, GPIO.LOW)

# Function for different LED patterns
def pattern_one():
    # LEDs light up one after the other then turn off together
    pass

def pattern_two():
    # All LEDs turn on and off simultaneously
    pass

def pattern_three():
    # LEDs light up and turn off in sequence
    pass

# Initialize variables
current_pattern = 1

try:
    while True:
        # Check if the button is pressed
        if GPIO.input(button) == GPIO.HIGH:
            current_pattern += 1  # Move to the next pattern
            if current_pattern > 3:
                current_pattern = 1  # Reset to the first pattern
            print(f"Pattern changed to: {current_pattern}")
            time.sleep(0.3)  # Debounce delay

        # Run the current pattern
        if current_pattern == 1:
            pattern_one()
        elif current_pattern == 2:
            pattern_two()
        elif current_pattern == 3:
            pattern_three()

except KeyboardInterrupt:
    pass

# Clean up GPIO settings
GPIO.cleanup()