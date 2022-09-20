from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_paddle_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_paddle_score, align=ALIGNMENT, font=FONT)

    def add_score(self, side):
        if side == "right":
            self.left_paddle_score += 1
        else:
            self.right_paddle_score += 1
        self.update_score()

    def game_over(self):
        if self.left_paddle_score == 5 or self.right_paddle_score == 5:
            winner = ""
            if self.left_paddle_score == 5:
                winner = "Left Paddle"
            else:
                winner = "Right Paddle"
            self.goto(0,0)
            self.write("Game Over", align=ALIGNMENT, font=FONT)
            self.goto(0, -100)
            self.write(f"{winner} wins!", align=ALIGNMENT, font=("Courier", 50, "normal"))
            return True
        

