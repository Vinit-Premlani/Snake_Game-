from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey (snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refesh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
        score.restart()
        snake.restart()
        

    # Detect collision with tail.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
        # If the head collides with any segment in the tail:
            score.restart()
            snake.restart()
            # Trigger game_over

screen.exitonclick()