import RPi.GPIO as GPIO
import time
import random

# Set up GPIO
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
# Set up component pins
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as output pin for LED
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set up GPIO13 as input pin with pull-down resistor

# Ensure the LED is off before starting
GPIO.output(18, GPIO.LOW)

# Initialize variables
score = 0 # User's score

try:
    while True: # Continuous loop to run the game
        # Generate random delay time before turning the LED on
        led_off = random.randint(2,10) # Random delay between 2 and 10 seconds
        time.sleep(led_off)

        # Turn LED on
        GPIO.output(18, GPIO.HIGH)
        start_time = time.time() # Record the start time

        # Check for button press while LED is on
        button_pressed = False
        while((time.time() - start_time) < 1):
            if(GPIO.input(13) == GPIO.HIGH): # If button is pressed within button turning on
                button_pressed = True
                break # Exit the loop if button is pressed

        # Turn the LED off
        GPIO.output(18, GPIO.LOW)

        # Update the score if button was pressed while LED was on
        if(button_pressed):
            score += 1
            print(f"Player Score: {score}")

        # Delay
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Clean up GPIO settings before exiting
GPIO.cleanup()
