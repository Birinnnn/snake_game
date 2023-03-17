from turtle import Turtle
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto(0, 250)
        self.update()
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
