import matplotlib.pyplot as plot
import matplotlib.animation as animation
import time
import random

def lightning(i, strikeMin, strikeMax, height, area, width):
    #Figure border (Lines in X and Y axis) forces a figure size.
    borderX = [0, 0, area]
    borderY = [height, 0, 0]
    
    #Lists for lightning travel path.
    strikeX = []
    strikeY = []

    #Direction is lightning "zigzag", distance is how far each zigzag will go downwards.
    direction = 0 #Idle. Replaced by "directionDerange. Will probably be used if I choose to add lightning rod.
    distance = 0
    tipX = 0
    tipY = 0

    source = 0 #Where the lighting comes from

    strikes = 0 #Number of total strikes.
    averageDistance = 0 #Length as value each strike will derange from.

    i = 1 #Counter starts after first strike, while the last point creates one strike. Therefore, only one strike subtracted in total.

    #Number of strikes, their length, and their direction.
    strikes = random.randint(strikeMin, strikeMax)
    averageDistance = height / strikes
    
    #First strike.
    tipY = height
    strikeY.append(tipY)

    source = random.uniform(0, area)
    tipX = source
    strikeX.append(tipX)
    plot.plot(strikeX, strikeY)

    
    while i <= strikes:
        #Finding each of their lengths.
        distanceDerange = averageDistance / 1.2
        distance = random.uniform(distanceDerange - averageDistance, averageDistance + distanceDerange)
        tipY = tipY - distance
        strikeY.append(tipY)

        #Finding each of their directions.
        directionDerange = random.uniform(width * -1, width)
        tipX = tipX + directionDerange
        strikeX.append(tipX)
        i = i + 1
        plot.plot(strikeX, strikeY)


    #Last strike.
    tipY = 0
    strikeY.append(tipY)

    finalXDerange = tipX / width #We want the final strike to go more or less downward.
    finalX = random.uniform(finalXDerange * -1, finalXDerange)
    tipX = tipX + finalX
    strikeX.append(tipX)

    #Plots border.
    plot.plot(borderX, borderY)

    plot.plot(strikeX, strikeY)


while True:
    ani = animation.FuncAnimation(plot.gcf(), lightning, fargs = (4, 15, 100, 500, 25,), interval = 5000)
    plot.show()




        






#First, find how many times we want the lightning to change direction (strikes), say, up to a maximum of 10.
#On average, each srtrike length must be total distance from cloud to ground, let's say 100. First strike must therefore start at height 100.
#Take that average, divert slightly from it from time to time to variate strike length, and make the last strike hit spot on the ground.
#Since each strike will get closer and closer to 100/10, swap them around randomly to make it look more natural.