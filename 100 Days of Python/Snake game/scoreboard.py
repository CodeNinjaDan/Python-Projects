from turtle import Turtle

#Use constants for easy code editing
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.update_scoreboard()

    #Create functions to reduce repetition.
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
    def track_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
