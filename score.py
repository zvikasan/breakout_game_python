from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lifes = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Lifes: {self.lifes}", align="left",
                   font=FONT)

    def life_lost(self):
        self.lifes -= 1
        self.update_scoreboard()

    def reset_score(self):
        self.lifes = 3
        self.update_scoreboard()
    
    def loose(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Game Over", align="left",
                   font=FONT)

    def win(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"You Win!!!", align="left",
                   font=FONT)




