import time
import turtle


oldTime = time.time()
newTime = 0


window = turtle.Screen()
window.title("Shapeshifter")
window.bgcolor("red")


class Shape(turtle.Turtle):
    def __init__(self, colors, shapes):
        turtle.Turtle.__init__(self)
        self.penup()
        self.colors = colors
        self.shapes = shapes
        self.frame = 0

    def animate(self):
        self.frame = self.frame + 1
        if self.frame == len(self.colors):
            self.frame = 0
        self.color(self.colors[self.frame])
        self.shape(self.shapes[self.frame])
        
        window.ontimer(self.animate, 500)


shape1Colors = ["black",
    "green",
    "blue"
]

shape1Shapes = [
    "triangle",
    "square",
    "circle"
]

shape2Colors = ["green",
    "blue",
    "green"
]

shape2Shapes = [
    "circle",
    "triangle",
    "square"
]

shape1 = Shape(shape1Colors, shape1Shapes)
shape1.goto(-100, 0)
shape1.animate()

shape2 = Shape(shape1Colors, shape1Shapes)
shape2.goto(100, 0)
shape2.animate()


while True:
    window.update()
    newTime = time.time()
    if newTime >= oldTime + 2:
        oldTime = newTime
        print("Test")



window.mainloop()