import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

turtle_instance=turtle.Turtle()

def turtleForward():
    turtle_instance.forward(100)
    
def turtleTurn():
    turtle_instance.left(90)
    
drawing_board.listen()
drawing_board.onkey(turtleForward,"space")
drawing_board.onkey(turtleTurn,"Up")

turtle.mainloop()