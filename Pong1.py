# Simple Pong game
import turtle
import os
wn = turtle.Screen()
wn.title("Pong by Rossco")
wn.bgcolor("aqua")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('violet')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('lime')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('violet')
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('purple')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Alien: 0 vs Predator: 0", align='center', font=('Courier', 24, 'normal'))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    x = paddle_a.ycor()
    x += -40
    paddle_a.sety(x)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -50
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w') # pressing w calls the paddle_a_up function
wn.onkeypress(paddle_a_down, 's') # pressing the s key calls the paddle_a_down function
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, 'l')



# Main game loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('aplay boop.wav&')

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('aplay boop.wav&')
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Alien: {} vs Predator: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Alien: {} vs Predator: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() -80):
        ball.setx(340)
        ball.dx *= -1
        os.system('aplay boop.wav&')

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() -80):
        ball.setx(-340)
        ball.dx *= -1
        os.system('aplay boop.wav&')