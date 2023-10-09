import random
import turtle


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