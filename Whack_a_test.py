import RPi.GPIO as GPIO 
import time 
import random
import I2C_LCD_driver

timerCondition = 0
def timer():
    global time1
    global time2
    global stopwatch
    global stopwatchResult

    stopwatch = time.time()
    if timerCondition == 0:
        waitTime = 3
        curveFlat = waitTime
        timerCondition = 1

    time1 = time.time()
    curveFlat = curveFlat / 1.1
    waitTime = waitTime * 0.8
    time2 = time1 + waitTime + curveFlat
    stopwatchResult = time.time() - stopwatch
 

GPIO.setmode(GPIO.BCM) 


#LEDs.
led1 = 21
led2 = 20
led3 = 16
led4 = 12
led5 = 7

#Buttons.
button1 = 8
button2 = 25
button3 = 18
button4 = 15
button5 = 14


points = 0

#"Tests" for the RNG.
tests = [led1, led2, led3, led4, led5]

#Buttons for the RNG.
buttons = [button1, button2, button3, button4, button5]

mylcd = I2C_LCD_driver.lcd()


GPIO.setup(led1, GPIO.OUT) 
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT) 
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)

GPIO.setup(button1, GPIO.IN) 
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN) 
GPIO.setup(button4, GPIO.IN)
GPIO.setup(button5, GPIO.IN)


#What's the range the RNG should pick from? The amount of buttons are the same as the amount of tests(one button per test).
testCount = len(tests)

try: 
    while True: 
        
        #Makes shure the same test isn't repeated.
        testValid = False
        currentTestMemory = 0
        while testValid == False:
            global currentTest
            currentTest = random.randint(0, testCount) #Currently active test.
            if not currentTest == currentTestMemory:
                testValid = True

        currentTestMemory = currentTest
        
        GPIO.output(tests[currentTest], True)

        global pointCount
        pointCount = 0 #Used to calculate your grade.

        pointValid = True #Condition for if a point is gained or not.
        
        timer()
        unpredictability = time2
        unpredictability = random.randint(unpredictability - stopwatchResult / 7, unpredictability + stopwatchResult / 7)

        while timer(time1) <= timer(unpredictability) and pointValid == True:
            time1 = time.time()

            if GPIO.input(buttons[currentTest]) == True:
                points = points + 1
                pointValid == False
        pointCount = pointCount + 1
        
        
        if stopwatchResult <= 0.2:
            break
            
    grade = points / pointCount * 6
    print(grade)


 


except KeyboardInterrupt: 
        print ("Cleaning up GPIO pins!")
        GPIO.cleanup()
        print ("Exiting program")