import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buzzer = 8

GPIO.setup(buzzer, GPIO.OUT)

try:
    while True:
        #Note pitch frequencies.
        high = 250
        medium = 200
        low = 150
        
        x = 0
        count = 0 #Counter.
        period = 0 #Time one frequency lasts.
        length = 0 #Note length in seconds.
        note = 0

        GPIO.output(buzzer, False)

        
        note = low #Note
        length = 0.5 #Note lasts for 4 seconds.
        pause = 0 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = medium #Note
        length = 1 #Note lasts for 4 seconds.
        pause = 0 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = low #Note
        length = 0.25 #Note lasts for 4 seconds.
        pause = 0 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = high #Note
        length = 2 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        #Left off here!
        x = 0
        time.sleep
        note = high #Note
        length = 0.3 #Note lasts for 4 seconds.
        pause = 5 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------
        x = 0
        time.sleep(pause)

        note = high #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = low #Note
        length = 1 #Note lasts for 4 seconds.
        pause = 0.1 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = medium #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep
        note = high #Note
        length = 0.3 #Note lasts for 4 seconds.
        pause = 5 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------
        x = 0
        time.sleep(pause)

        note = high #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = low #Note
        length = 1 #Note lasts for 4 seconds.
        pause = 0.1 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = medium #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep
        note = high #Note
        length = 0.3 #Note lasts for 4 seconds.
        pause = 5 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------
        
        x = 0
        time.sleep(pause)

        note = high #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = low #Note
        length = 1 #Note lasts for 4 seconds.
        pause = 0.1 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)
        note = medium #Note
        length = 4 #Note lasts for 4 seconds.
        pause = 2 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep
        note = high #Note
        length = 0.3 #Note lasts for 4 seconds.
        pause = 5 #Pause between notes.
        
        period = 1 / note #250 swings per second.
        count = (note * length) #The freqency repeats the loop enought times to give one second, times note length.

        while x <= count:
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(period / 2)
            print(x)
            x = x + 1

            #New note -----------------------

        x = 0
        time.sleep(pause)


except KeyboardInterrupt:
    print("Reset")
    GPIO.cleanup()