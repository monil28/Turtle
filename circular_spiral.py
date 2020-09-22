import turtle
monil = turtle.Turtle()
monil.speed(15)
def square(length,angle,main_angle):
 for j in range(3):
  monil.forward(length)
  monil.right(angle)
 monil.forward(length)
 monil.right(main_angle)
for i in range(56):
 square(100,90,95)

monil.exitonclick()
