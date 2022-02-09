from tkinter import W
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver

char1Pos = 0 #Position of character on LCD screen.
char2Pos = 15

mylcd = I2C_LCD_driver.lcd() #Defines first and only peripheral.


try:
    mylcd.lcd_clear()
    while True:
        mylcd.lcd_display_string_pos("a", 1, char1Pos)
        while char1Pos < 15:    
            char1Pos = char1Pos + 1
            char2Pos = char2Pos -1

            mylcd.lcd_display_string_pos("a", 1, char1Pos)
            mylcd.lcd_display_string_pos("a", 2, char2Pos)
                
            time.sleep(0.5)
            mylcd.lcd_clear()

        while char1Pos >= 1:
            char1Pos = char1Pos -1
            char2Pos = char2Pos +1
            
            mylcd.lcd_display_string_pos("a", 1, char1Pos)
            mylcd.lcd_display_string_pos("a", 2, char2Pos)
            
            time.sleep(0.5)
            mylcd.lcd_clear()


except KeyboardInterrupt:
    GPIO.cleanup()
    print("Clean!")