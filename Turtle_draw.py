import turtle

def draw_square():
	window = turtle.Screen()
	#window.bgcolor("blue")

	brad = turtle.Turtle()
	brad.speed(800)

	turtle.color("yellow","yellow")
	
	m = 0
	n = 0
	turtle.begin_fill()
	while n != 360:
		brad.color("red")
		while m != 4:
			brad.forward(100)
			brad.right(90)
			m += 1
		brad.right(1)
		m = 0
		n += 1
	turtle.end_fill()

	window.exitonclick()

draw_square()