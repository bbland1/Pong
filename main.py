from turtle import Turtle, Screen, right
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Setting up the screen of the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
# Makes is so the screen doesn't refresh so quickly you can't see anything
screen.tracer(0)

# Setting up the game components
left_paddle = Paddle((-360, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

# getting the screen to listen and what to listen for each paddle
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

# Starting the game
game_started = True

while game_started:
    # changes the speed of the screen basically pausing
    time.sleep(ball.move_speed)
    # the changes of the screen update
    screen.update()
    # game gets moving
    ball.move()

    # Detect the top and bottom wall collision and make the ball bounce
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect the collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 and ball.x_move > 0 or ball.distance(left_paddle) < 50 and ball.xcor() < -345 and ball.x_move < 0:
        ball.bounce_x()

    # Detect if the paddles miss the ball
        # Right paddle missing
    if ball.xcor() > 380 and ball.x_move > 0:
        ball.reset()
        score.add_score("right")

        # Left paddle missing
    if ball.xcor() < -390 and ball.x_move < 0:
        ball.reset()
        score.add_score("left")

    #  Detects if either player has reached 5 first and whoever has wins
    if score.game_over():
        game_started = False

screen.exitonclick()
