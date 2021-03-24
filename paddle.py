# from main import STARTING_POSITION
from turtle import Turtle

MOVE_DISTANCE = 20
# STARTING_POSITION = (350, 0)


class Paddle(Turtle):
    def __init__(self, starting_position, play_area):
        super().__init__()
        self.create_paddle(starting_position)
        self.play_area = play_area[0]
        # self.speed = 10

    def create_paddle(self, starting_position):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def go_right(self):
        if ((self.xcor()+MOVE_DISTANCE) < (self.play_area/2 - 40)):
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_left(self):
        if ((self.xcor()-MOVE_DISTANCE)>(30-self.play_area/2)):
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
