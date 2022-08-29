import math
import turtle


window = turtle.Screen()
drawer1 = turtle.Turtle()
drawer2 = turtle.Turtle()

window.title("Drawing")
window.bgcolor("white")

counter = 110

# drawer1.penup()
# drawer1.goto(-500, -750)
# drawer2.penup()
# drawer2.goto(-1000, -750)

# for i in range(1000):
#      v1 = 10*2*math.pi*i/1000
#      y1 = 250 + 250 * math.sin(v1)
#      if i == 0:
#          drawer1.goto(i, y1 - 250)
#          drawer1.pendown()
#      drawer1.goto(i, y1 - 250)
     
#      v2 = i * 100
#      y2 = 250 * math.sin(v2)
#      if i == 0:
#          drawer2.goto(i - 500, y2 - 250)
#          drawer2.pendown()
#      drawer2.goto(i - 500, y2 - 250)

drawer1.pendown()
for i in range(1000):
    #v = i * 0.2
    #y = math.sin(v) * 100
    #if i == 0:
    #    drawer1.goto(i, y)
    #    drawer1.pendown()
    #drawer1.goto(i, y)
    v = i / 1000 / 8 * 100
    y = math.sin(v)
    drawer1.goto(i, y * 100)
    
#while True:
    # drawer.color("green")
    # drawer.forward(counter)
    # drawer.left(150)
    # drawer.color("blue")
    # drawer.forward(counter)
    # drawer.left(165)
    # counter = counter + (counter/(counter/3))

    

turtle.done()