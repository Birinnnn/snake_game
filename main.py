from turtle import Screen
from snake import Snake
import time
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Eating the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # Hit the wall
    x_coord = snake.head.xcor()
    y_coord = snake.head.ycor()
    if x_coord > 280 or x_coord < -280 or y_coord > 280 or y_coord < -280:
        game_is_on = False

    # Hit the tail
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False

scoreboard.over()
screen.exitonclick()
