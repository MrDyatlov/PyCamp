import random
import turtle

tBoard = turtle.Screen()
tBoard.title("Catch Kenny")
tBoard.bgcolor("light blue")


score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
grid_size = 10
score = 0
turtle_list = []


def setup_score_turtle():
    score_turtle.penup()
    score_turtle.hideturtle()

    top_height = turtle.window_height() / 2
    y = top_height * 0.85
    score_turtle.goto(0, y)
    score_turtle.write("Score: {}".format(0), font=("Bahnschrift", 25, "bold"), align="center")




def make_turtle(x, y):
    kenny = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), font=("Bahnschrift", 25, "bold"), align="center")

    kenny.onclick(handle_click)
    kenny.shape("turtle")
    kenny.shapesize((1))
    kenny.penup()
    kenny.speed(100)
    kenny.goto(x * grid_size, y * grid_size)
    turtle_list.append(kenny)


def countdown(time):
    countdown_turtle.penup()
    countdown_turtle.hideturtle()

    top_height_cd = turtle.window_height() / 2
    yy = top_height_cd * 0.75
    countdown_turtle.goto(0, yy)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time), font=("Bahnschrift", 20, "normal"), align="center")
        turtle.ontimer(lambda: countdown(time - 1), 1000)
    else:
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over B*tch!", font=("Bahnschrift", 20, "normal"), align="center")
        exit(tBoard.mainloop())


x_cors = [30, 20, 10, 00, -10, -20, -30]
y_cors = x_cors[::-1]
y_cors.remove(30)


def grid_turtle():
    for y in y_cors:
        for x in x_cors:
            make_turtle(x, y)


def hide_turtles():
    for ken in turtle_list:
        ken.hideturtle()


diff = turtle.numinput("Diff", "Enter", 5, minval=1, maxval=10)
last_diff = int(diff) * 100


def random_turtle():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    turtle.hideturtle()
    global last_diff
    tBoard.ontimer(random_turtle, last_diff)


timer = turtle.numinput("Time", "Enter", 30, minval=1, maxval=90)
last_timer = int(timer)


def start_game_up():
    turtle.tracer(0)

    grid_turtle()
    setup_score_turtle()
    countdown(last_timer)
    hide_turtles()
    random_turtle()

    turtle.tracer(1)
start_game_up()
tBoard.mainloop()
