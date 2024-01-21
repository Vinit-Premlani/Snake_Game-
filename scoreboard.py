from turtle import Turtle
ALINGNMENT = "center"
FONT = ("Courier",22,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake Game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(x=0,y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALINGNMENT, font=FONT)

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake Game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard() 

    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write("GAME OVER.", align=ALINGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
