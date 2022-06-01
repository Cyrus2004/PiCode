#RPi.GPIO for use of GPIO pins, time imports a stopwatch
import RPi.GPIO as GPIO #Imports the part of the library RPi called GPIO, as just GPIO.
import time
GPIO.setmode(GPIO.BCM)

#Gives the inputs and outputs names by putting them in variables.
trig = 16 #BCM for the trig-pin for the sensor
echo = 20 #BCM for the echo-pin on the sensor.
button = 18 #BCM for input from the button.
yellow = 23 #BCM for signal to yellow LED.
red = 24 #BCM for signal to red LED.
ir = 25 #BCM for input from IR sensor.
buzzer = 8 #BCM for signal to the buzzer.

#Variables for storing inputs.
key = 0 #Push button state.
irSig = 0 #Burglar arrived?

#Sets inputs and outputs of GPIO pins.
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(button, GPIO.IN)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(ir, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


try: #Interrupts loop if except is triggered.
    #Functionality of the circuit
    while True:
        #Sets inputs to actively low.
        GPIO.output(trig, False)
        GPIO.output(yellow, False)
        GPIO.output(red, False)
        GPIO.output(buzzer, False)
        time.sleep(0.05) #Gives time to switch to actively low.
        
        
        #Ultrasonic distance measurement.
        
        #Sensor outputs eight pulses of ultrasonic signals.
        #Sends eight pulses within ten microseconds.
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        #pulseIn
        #Measures signal travel time.
        while GPIO.input(echo)==0: #The input from echo is fed right in. Loop runs as long as echo is LOW, while the sound travels.
            pulseStart = time.time() #pulseStart is used in relation to pulseEnd, and updates while the loop runs.

        while GPIO.input(echo)==1: #The loop will run while echo is high.
            pulseEnd = time.time() #pulseEnd is updated until echo goes to 0, when the sound signal has traveled back again.

        duration = pulseEnd - pulseStart #Pulse duration found by finding difference between pulseStart and pulseEnd.

        #measure distance
        distance = (duration * 17150) #Duration times speed of sound is distance. Divided by two to get the distance one way, and not both.

        #Stores button state
        key = GPIO.input(button)


        #Lights yellow and red diodes of key is activated, and the owner walks in.
        if distance <= 25 and key == True: #Checks if owner, who has the "key", is home.
            
            #Sends signals to diodes
            GPIO.output(yellow, True)
            time.sleep(5) #Keep the door(yellow LED), open for five seconds.
            GPIO.output(yellow, False) #Locks the door.
            
            #Keeps the lights indoors(red LED) on until owner leaves and presses the key.
            key = GPIO.input(button)
            while key == False: #Light is on while owner is indoors. Welcome home!
                GPIO.output(red, True)
                key = GPIO.input(button) #Checks every time to see if owner left, and pressed the button again.
            GPIO.output(red, False) #Turns off the lights.

        irSig = 1 - GPIO.input(ir) #Stores IR input. Signal i HIGH when sensor is not triggered, so 1-GPIO.input(ir) inverts it.

        #Sounds the alarm if a someone broke in.
        if irSig == True and key == False: #Checks if someone without a key broke in.
            while True: #Loop keeps the alarm going.
                #Turns the buzzer on and off with a frequency of 400Hz, to create sound.
                GPIO.output(buzzer, True)
                time.sleep(0.0050 / 2) #Delay between switching of sound is halved by two, to get half a cycle.
                GPIO.output(buzzer, False)
                time.sleep(0.0050 / 2) #Delay between switching of sound is halved by two, to get half a cycle.

                #Stops the alarm if the button is pressed.
                key = GPIO.input(button)
                if key == True:
                    break #Exits the loop.


except KeyboardInterrupt:
        print ("Cleaning up GPIO pins!")
        #Resetter GPIO-pinnene.
        GPIO.cleanup()
        print ("Exiting program")
