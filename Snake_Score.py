import turtle


class Score:
    def __init__(self):
        f = open("Highest_score_snake.txt", "r")
        self.high_score = int(f.read())
        f.close()
        self.score = 0
        self.title = turtle.Turtle()
        self.title.color("white")
        self.title.speed(0)
        self.title.hideturtle()
        self.title.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.title.clear()
        self.title.write(f"Score: {self.score} Highest Score {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.high_score < self.score:
            with open("Highest_score_snake.txt", "w") as f:
                f.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_score()
