import RPi.GPIO as GPIO
import time

# Set up GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Define pin numbers using the physical pin numbering (Any pin can Join)
LED_PIN = 5  # Example: pin 11 (physical pin number)
BUTTON_PIN = 3  # Example: pin 7 (physical pin number) sensor_pin

# Set up pins as input or output
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn ON LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn OFF LED
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO pins on exit
    GPIO.cleanup()
