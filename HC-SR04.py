import RPi.GPIO as GPIO 

import time 

 

GPIO.setmode(GPIO.BCM) 

 

echo =15 

trig =14 

 

GPIO.setup(echo, GPIO.IN) 

GPIO.setup(trig, GPIO.OUT)

 

try: 

    while True: 

        GPIO.output(trig, False) 

        time.sleep(2) 

 

        GPIO.output(trig, True) 

        time.sleep(0.00001) 

        GPIO.output(trig, False)

 

        #pulseIn maler tiden.  

        while GPIO.input(echo)==0: 

            pulseStart = time.time()
            print("Test")

 

        while GPIO.input(echo)==1: 

            pulseEnd = time.time()

 

        duration = pulseEnd - pulseStart 

 

        #measure distance 

        distance = duration * 17150 

 

        distance = round(distance, 2) 

        print ("Distance: ", distance, "cm") 

except KeyboardInterrupt: 

        print ("Cleaning up GPIO pins!")

        GPIO.cleanup()

        print ("Exiting program")