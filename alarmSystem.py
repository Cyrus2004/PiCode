import RPi.GPIO as GPIO
import I2C_LCD_driver #Driver for I2C protocol for LCD
import time

GPIO.setmode(GPIO.BCM)

switch = 18
buzzer = 14

trig = 23
echo = 24

mylcd = I2C_LCD_driver.lcd() #Referer til LCD-en som kjører på driveren.

switchSig = 0

GPIO.setup(switch, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


try:
    switchSig = GPIO.input(switch) #Checks the status of smart switch.
    while True:
        
        #Shows the distance on the lcd screen while smart switch is off, meaning no one broke in.
        while switchSig == 0:
            

            #Measures distance.

            #Gives the trigger pin time to reset.
            GPIO.output(trig, False)
            time.sleep(0.1)

            #Tells the sensor to output eight pulses of ultrasonic signals.
            GPIO.output(trig, True)
            time.sleep(0.00001) #Ten microseconds between each pulse.
            GPIO.output(trig, False)

            
            #Measures sound travel time.
            
            #pulseStart updates until signal is sent, pulseEnd updates until signal is recieved. Epoch(time value) is universal.
            while GPIO.input(echo)==0:
                pulseStart = time.time()

            while GPIO.input(echo)==1:
                pulseEnd = time.time()

            duration = pulseEnd - pulseStart #Sound travel time is difference between signal sent and signal recieved.

            #measure distance
            distance = duration * 34300 / 2 #Distance = Time(duration) * Speed(of sound) / 2(sound travel time both ways, not one.)

            #Rounds off the distance to the nearest hundreth decimal.
            distance = round(distance, 2)


            #Prints the result
            mylcd.lcd_clear() #Readies for next frame
            mylcd.lcd_display_string("Distance:", 1) #Character 1, line 1. Line is default.
            mylcd.lcd_display_string_pos(str(distance), 2, 4) #Character 4, line 2. str() changes integer to string so the lcd cam understand it.

            #Checks if switch status has changed.
            switchSig = GPIO.input(switch)
            
            time.sleep(1)#Slow down!

        #If someone broke in, the above while-loop won't run. Another while-loop is therefore not necessary here.
        mylcd.lcd_display_string("Distance:", 1)
        #mylcd.clear isn't necessary since frame doesen't change. Therefore, no need for wait time!

        while switchSig == 1: #Loop keeps the alarm going while someone broke in.
            #Turns the buzzer on and off with a frequency of 400Hz, to create sound.
            GPIO.output(buzzer, True)
            time.sleep(0.0050 / 2) #Delay between switching of sound is halved by two, to get half a cycle.
            GPIO.output(buzzer, False)
            time.sleep(0.0050 / 2) #Delay between switching of sound is halved by two, to get half a cycle.
            
            #switchSig = GPIO.input(switch) Checks if smart switch status has updated.


except KeyboardInterrupt:
    print("Cleaning up GPIO pins!")
    GPIO.cleanup()
    print("Exiting program.")
