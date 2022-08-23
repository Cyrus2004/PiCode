#Translate any RPi GPIO configurations to configurations of specific microcontroller.

import RPi.GPIO as GPIO
import time
import I2C_LCD_driver


#Set GPIO mode if relevant.

magnet = 1
restart = 2
mylcd = I2C_LCD_driver.lcd()

#Set GPIO inputs and outputs.


diameter = 13 #Rotary part of motor plus magnet height. Used to calculate circumference.
circumference = diameter * 3.14159

depth = 0 #Anchor depth


while True:
    depth = int(depth)
    magnetState = 0 #Stays low if magnet isn't passing.
    
    magnetState = GPIO.input(magnet)
    
    #Magnet has gone from low to high and to low again, and so it has passed!
    while magnetState == True:
        time.sleep(0.05) #Avoids hysterisis.
    
    depth = depth + circumference
    magnetState = GPIO.input(magnet)
        
    if GPIO.input(restart) == True:
        magnetState = 0

    #Updates screen.
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Ankerdybde:", 1)
    mylcd.lcd_display_string_pos(str(depth), 2, 4)

    #How to guess and "update" anchor depth between rotations:
        #1. Mesure the amount of time the previous rotation took.
        #2. The amount of distance the anchor has dropped will be the circumference of the anchor divided by the time times the time step: D = C / T * S.
        #3. The total anchor drop length is updated to a definite value each time the magnet passes.
        #4. If the magnet takes more than five seconds to pass or the estimated anchor drop between magnet passes is more than the circumference, the number is reset to previous definite value.