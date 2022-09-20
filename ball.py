from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Getting the ball to move in general
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Change the direction if the ball hits the top or bottom wall
    def bounce_y(self):
        self.y_move *= -1

    # Change the direction and the speed when the ball hits a paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # reset when the ball goes out of bounds
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
