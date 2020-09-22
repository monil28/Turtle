import turtle
turtle.shape('turtle')
turtle.bgcolor("black")
turtle.speed(0)

for i in range(35):
	turtle.color("red")
	turtle.circle(100)		# radius
	turtle.left(10)

turtle.mainloop()