import time
import turtle


oldTime = time.time()
newTime = 0


window = turtle.Screen()
window.title("Shapeshifter")
window.bgcolor("red")

sprite = turtle.Turtle()
sprite.shape("triangle")


def sprite_animate():
    if sprite.shape() == "triangle":
        sprite.shape("circle")
    else:
        sprite.shape("triangle")
    
    window.ontimer(sprite_animate, 500)
sprite_animate()


while True:
    window.update()
    newTime = time.time()
    if newTime >= oldTime + 2:
        oldTime = newTime
        print("Test")



window.mainloop()