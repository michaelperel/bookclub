from RPi import GPIO
import time

# Pin Setup:
GPIO.setmode(
    GPIO.BCM
)  # Broadcom pin-numbering scheme. This uses the pin numbers that match the pin numbers on the Pi Traffic light.
GPIO.setup(9, GPIO.OUT)  # Red LED pin set as output
GPIO.output(9, True)  # Turns on the Red LED

GPIO.setup(10, GPIO.OUT)  # Yellow LED pin set as output
GPIO.output(10, True)  # Turns on the Yellow LED

GPIO.setup(11, GPIO.OUT)  # Green LED pin set as output
GPIO.output(11, True)  # Turns on the Green LED

time.sleep(5)
GPIO.output(9, False)  # Turns off the Red LED
GPIO.output(10, False)  # Turns off the Red LED
GPIO.output(11, False)  # Turns off the Red LED

GPIO.cleanup()
