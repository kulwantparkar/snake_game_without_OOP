from turtle import Screen, Turtle
import time

import random

screen = Screen()
screen.title("My Snake Game")
screen.setup(height=500, width=600)
screen.bgcolor("black")
screen.tracer(0)

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("red")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)
        self.goto(rand_x, rand_y)

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.cobra = []
        self.create_snake()
        self.head = self.cobra[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        kai = Turtle()
        kai.color("white")
        kai.shape("square")
        kai.penup()
        kai.goto(position)
        self.cobra.append(kai)

    def extend(self):
        self.add_segment(self.cobra[-1].position())

    def move(self):
        for coco in range(len(self.cobra)-1, 0, -1):
            x_position = self.cobra[coco-1].xcor()
            y_position = self.cobra[coco - 1].ycor()
            self.cobra[coco].goto(x_position, y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for seg in snake.cobra[1:]:
        if snake.head.distance(seg) < 10:
            is_on = False
            scoreboard.game_over()

    snake.move()

screen.exitonclick()