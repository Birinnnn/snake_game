from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        print(self.head.position())

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_tail(position)

    def add_tail(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        self.add_tail(self.body[-1].position())

    def move(self):
        for num in range(len(self.body) - 1, 0, -1):
            self.body[num].goto(self.body[num - 1].xcor(), self.body[num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
