from turtle import Turtle
FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over_text(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGNMENT,
                   font=FONT)
