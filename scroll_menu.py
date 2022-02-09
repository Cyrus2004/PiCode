from tkinter import W
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver

GPIO.setmode(GPIO.BCM)

yAxis = 17 #Joystick Y-axis

lcd = I2C_LCD_driver.lcd()

GPIO.setup(yAxis, GPIO.IN)


try:
    while True:
        stateY = 0 #Joystick's Y-axis state
        line = 0 #What line am I on?

        stateY = GPIO.input(yAxis) #Stores joystick's state
        
        if stateY == 1:
            line = line + 1

        if stateY == 0:
            line = line - 1

        #if line > 4:
            #line = 0

        #if line < 1:
            #line = 4

        time.sleep(0.5) #Time delay for menu scrolling

        print(line)



except KeyboardInterrupt:
    print("Reset")
    GPIO.cleanup()