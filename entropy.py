import time
import random
import matplotlib.pyplot as plot
import matplotlib.animation as animation

valueX = 0
valueY = 0

highestValue = 0 #Highest figure X/Y coordinates, used to make the figure as much in X as in Y.


i = 0

xWalk = []
yWalk = []


# def animate(i):
#     plot.cla()
    
#     incrementX = random.randint(-100, 100)
#     global valueX
#     valueX = valueX + incrementX
#     incrementY = random.randint(-100, 100)
#     global valueY
#     valueY = valueY + incrementY
#     xWalk.append(valueX)
#     yWalk.append(valueY)
#     plot.plot(xWalk, yWalk)

#     i = i + 1
#     if i == 10000:
#         exit()                

    #global highestValue
    #if valueX > highestValue:
        #highestValue = valueX
    #if valueY > highestValue:
        #highestValue = valueY

#fig = plot.figure
#ani = animation.FuncAnimation(plot.gcf(), animate, interval = 0)

def animate(i):
    plot.cla()
    i = 0
    valueX = 0
    valueY = 0
    xWalk = []
    yWalk = []

    while i <= random.randint(1000, 100000):
        incrementX = random.randint(-100, 100)
        valueX = valueX + incrementX
        incrementY = random.randint(-100, 100)
        valueY = valueY + incrementY
        xWalk.append(valueX)
        yWalk.append(valueY)

        i = i + 1
    plot.plot(xWalk, yWalk)

while True:
    ani = animation.FuncAnimation(plot.gcf(), animate, interval = 5000)
    plot.show()

