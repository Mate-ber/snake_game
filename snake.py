import turtle
import random
import time

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=650, height=650)
window.tracer(0)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()

    def create_snake(self):
        positions = [(0, 0), (20, 0), (40, 0)]
        for i in range(3):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(positions[i][0], positions[i][1])
            self.segments.append(segment)
        self.head = self.segments[0]

    def move(self):

        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def change_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def change_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def change_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def change_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def extend(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.color("red")
        self.food.shape("circle")
        self.food.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)

    def new_food(self):
        self.food.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
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
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.update_score()


snake = Snake()
food = Food()
score = Score()

window.listen()
window.onkeypress(snake.change_up, "Up")
window.onkeypress(snake.change_down, "Down")
window.onkeypress(snake.change_right, "Right")
window.onkeypress(snake.change_left, "Left")


def start_again():
    score.reset_score()
    snake.head.goto(40, 0)
    for i in range(len(snake.segments)):
        snake.segments[i].goto(1000, 1000)
    snake.segments.clear()
    snake.create_snake()


while True:
    window.update()

    if snake.head.distance(food.food) < 20:
        score.increase_score()
        food.new_food()
        snake.move()
        snake.extend()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        start_again()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            start_again()
            snake.move()
            break

    snake.move()
    time.sleep(0.1)

window.mainloop()
