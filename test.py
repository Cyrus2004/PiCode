import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

test = 14

GPIO.setup(16, GPIO.IN)

try:
    while True:
        result = GPIO.input(16)
        time.sleep(0.5)
        print(result)

except KeyboardInterrupt:
    GPIO.cleanup()