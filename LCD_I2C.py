import RPi.GPIO as GPIO
import I2C_LCD_driver
import time

GPIO.setmode(GPIO.BCM) 

echo =20 
trig =16

mylcd = I2C_LCD_driver.lcd()


GPIO.setup(echo, GPIO.IN) 
GPIO.setup(trig, GPIO.OUT)


#Makes shure that trig is set to low.
try: #Debugging
    while True: #Runs the loop again and again.
        GPIO.output(trig, False)#Sets the output for trig to False, or LOW. 
        time.sleep(0.1) #Two seconds pause.

        #Tells the sensor to output eight pulses of ultrasonic signals.
        GPIO.output(trig, True)
        time.sleep(0.00001) #Sends eight pulses withing ten microseconds(the signal from trig(GPIO24).
        GPIO.output(trig, False)

        #pulseIn
        #Measures the time it takes for the sound to travel to and from.
        while GPIO.input(echo)==0: #The input from echo is fed right in. As long as echo is low, that's when there is no signal going through the air, the loop will runø
            pulseStart = time.time() #pulseStart is updated continuisly while the loop is running. his point of time is therefore used in relation to pulseEnd.

        while GPIO.input(echo)==1: #The loop will run while echo is high.
            pulseEnd = time.time() #pulseEnd is updated until echo goes to 0, when the sound signal has traveled back again.

        duration = pulseEnd - pulseStart #Time's value after the signal was sent is subtracted from the value time had after the pulse ended, to find the pulse's duration.

        #measure distance
        distance = duration * 17150 #The distance is calculated by timing duration with the speed of sound. The speed is already divided by two, instead of dividing the whole calculation with two afterward.

        #Rounds off the distance to the nearest hundreth decimal.
        distance = round(distance, 2)

        #Prints the result
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Distance:", 1)
        mylcd.lcd_display_string_pos(str(distance), 2, 4)
        print(distance)
        time.sleep(1)


except KeyboardInterrupt:
        print ("Cleaning up GPIO pins!")
        #Resets GPIO pins.
        GPIO.cleanup()
        print ("Exiting program")