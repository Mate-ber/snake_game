import turtle


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
