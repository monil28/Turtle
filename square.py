# making a square
import turtle
monil = turtle.Turtle()
monil.shape("classic")
monil.shapesize(1,5,10)
turtle.bgcolor("blue")

def square(length,angle):
 monil.forward(length)
 monil.right(angle)
 monil.forward(length)
 monil.right(angle)
 monil.forward(length)
 monil.right(angle)
 monil.forward(length)


for i in range(8):
    square(50,90)



monil.exitonclick()