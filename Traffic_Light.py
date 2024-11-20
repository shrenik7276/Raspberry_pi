import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(11, GPIO.OUT)  # Red LED
GPIO.setup(13, GPIO.OUT)  # Yellow LED
GPIO.setup(15, GPIO.OUT)  # Green LED

# Traffic light sequence
try:
    while True:
        GPIO.output(11, GPIO.HIGH)  # Red ON
        GPIO.output(13, GPIO.LOW)   # Yellow OFF
        GPIO.output(15, GPIO.LOW)   # Green OFF
        time.sleep(5)  # Red for 5 seconds

        GPIO.output(11, GPIO.LOW)   # Red OFF
        GPIO.output(13, GPIO.HIGH)  # Yellow ON
        GPIO.output(15, GPIO.LOW)   # Green OFF
        time.sleep(2)  # Yellow for 2 seconds

        GPIO.output(11, GPIO.LOW)   # Red OFF
        GPIO.output(13, GPIO.LOW)   # Yellow OFF
        GPIO.output(15, GPIO.HIGH)  # Green ON
        time.sleep(5)  # Green for 5 seconds

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO pins on exit
