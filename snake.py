import turtle
import time
from Snake_body import Snake
from Snake_Food import Food
from Snake_Score import Score

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=650, height=650)
window.tracer(0)


snake = Snake()
food = Food()
score = Score()

window.listen()
window.onkeypress(snake.change_up, "Up")
window.onkeypress(snake.change_down, "Down")
window.onkeypress(snake.change_right, "Right")
window.onkeypress(snake.change_left, "Left")


def start_again():
    score.reset_title()
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
