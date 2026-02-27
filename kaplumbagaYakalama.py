import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Kaplumbağa Yakala")
FONT = ("Arial", 30, "normal")

score = 0
game_over=False
#score_turtle'ı dışarıda tanımlıyoruz ki her fonksiyon erişebilsin.
score_turtle = turtle.Turtle()
count_down_turtle= turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.90
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)
    
grid_size = 10
turtle_list = []

def make_turtle(x, y):
    t = turtle.Turtle()
    
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
        
    t.penup()
    t.onclick(handle_click)
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)
    
x_koordinat = [-20, -10, 0, 10, 20]
y_koordinat = [20, 10, 0, -10]

def setup_turtle(): 
    for x in x_koordinat:
        for y in y_koordinat:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
        
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,750)
    else:
        hide_turtles()
    
    
def count_down(time):
    global game_over
    count_down_turtle.hideturtle()
    count_down_turtle.color("dark blue")
    count_down_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.90
    count_down_turtle.setpos(0, y-40)
    count_down_turtle.clear()
    
    if time>0:
        count_down_turtle.clear()
        count_down_turtle.write(arg=f"Zaman: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda:count_down(time-1),1000)
    else:
        game_over=True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
    
    
    
turtle.tracer(0)
setup_score_turtle()
count_down(10)
setup_turtle()
hide_turtles()
show_turtles_randomly()
turtle.tracer(1)

turtle.mainloop()