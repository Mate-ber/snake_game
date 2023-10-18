import turtle

file_name = "Highest_score_snake.txt"


class Score:
    def __init__(self):
        self.create_score()
        self.high_score = self.read_score()
        self.score = 0
        self.title = turtle.Turtle()
        self.title.color("white")
        self.title.speed(0)
        self.title.hideturtle()
        self.title.goto(0, 260)
        self.update_title()

    def update_title(self):
        self.title.clear()
        self.title.write(f"Score: {self.score} Highest Score {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_title()

    def reset_title(self):
        if self.high_score < self.score:
            self.change_score()
        self.score = 0
        self.update_title()

    def read_score(self):
        f = open(file_name, "r")
        num = int(f.read())
        f.close()
        return num

    def change_score(self):
        with open(file_name, "w") as f:
            f.write(str(self.score))
            self.high_score = self.score

    def create_score(self):
        if not self.check_exists():
            f = open(file_name, "x")
            f.write("0")
            f.close()

    def check_exists(self):
        try:
            with open(file_name, "r"):
                return True
        except FileNotFoundError:
            return False
