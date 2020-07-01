#Pong Python3

import turtle
import winsound

wn = turtle.Screen()
wn.title("Play Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops the window from updating itself, speeds up the game

# Score
score_a, score_b = 0, 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) 
# not the speed for the paddle on the screen, just the speed of the animation,
# we need to set this up fo the turtle module,
# this sets the speed to the maximum possible value, else it will be too slow
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() 
#turtles by default draw a line when they are moving,
# we dont need to do that so we pull the pen up
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# everytime our ball moves these numbers signify the no.
# of pixels the ball will move
ball.dx = 0.3 # in the x direction
ball.dy = -0.3 # in the y direction

#pen
pen = turtle.Turtle()
pen.speed(0) # animation speed, not the movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking : bounce off the border
    # for top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # add sound (wav) file here
        winsound.PlaySound("", winsound.SND_ASYNC)

    # for bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)

    # for right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    # for left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    # for paddle b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)

    # for paddle a
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)