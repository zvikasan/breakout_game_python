import random
from turtle import (Turtle)
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]


class BlockBuilder():

    def __init__(self):
        self.row_1 = []
        self.row_2 = []
        self.row_3 = []
        self.row_4 = []

    def __create_row__(self,row,screen_size):
        row_arr = []
        x_cor = 0 - screen_size[0]/2
        y_cor = screen_size[1]/2 -(100 + row*24)
        while x_cor < screen_size[0]/2 - 40:
            new_block = Turtle("square")
            new_block.shape("square")
            stretch_length = random.randint(2,4)
            new_block.shapesize(stretch_wid=1, stretch_len=stretch_length)
            new_block.color(random.choice(COLORS))
            new_block.penup()
            new_block.goto((x_cor, y_cor))
            row_arr.append(new_block)
            x_cor += stretch_length*25
        return row_arr
    
    def create_wall(self, screen_size):
        self.row_1 = self.__create_row__(1, screen_size)
        self.row_2 = self.__create_row__(2, screen_size)
        self.row_3 = self.__create_row__(3, screen_size)
        self.row_4 = self.__create_row__(4, screen_size)

    def redraw(self):
        for block in self.row_1:
            block.clear()


