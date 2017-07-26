import turtle

def draw_graph():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.right(60)
	for m in range(3):
		for n in range(3):
			for i in range(3):
				brad.color('green','green')
				brad.begin_fill()
				for j in range(3):
					brad.forward(30)
					brad.right(120)
				brad.end_fill()
				brad.forward(30)
				if i == 1:
					brad.right(120)
					brad.forward(30)
			if n != 1:
				brad.left(120)
			else: 
				brad.right(180)
				brad.forward(30 * 2)
				brad.left(60)
		brad.right(120)
		if m == 1:
			brad.right(120)
			brad.forward(30 * 4)
	window.exitonclick()

draw_graph()



