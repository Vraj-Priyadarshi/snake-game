import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_sco.txt") as data:
            content = data.read()
            s = int(content)
        self.high_score = s
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score ={self.score}", align="center", font=("Arial" , 18, "normal"))
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score ={self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_sco.txt", "w") as data:
                x = str(self.high_score)
                data.write(x)
        self.score = 0
        self.update_scoreboard()

