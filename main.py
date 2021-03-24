from turtle import Screen
from ball import Ball
from paddle import Paddle
from blocks import BlockBuilder
from score import Scoreboard
import time
from tkinter import messagebox

STARTING_POSITION = (0, -270)
SCREEN_SIZE = (800,600)


def init_game():
    global screen, score, ball, wall, paddle
    
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Breakout")
    screen.tracer(0)

    wall = BlockBuilder()
    wall.create_wall(SCREEN_SIZE)
    paddle = Paddle(STARTING_POSITION,SCREEN_SIZE)
    ball = Ball(SCREEN_SIZE)

    score = Scoreboard()

    screen.listen()
    screen.update()
    screen.onkeypress(paddle.go_left, "Left")
    screen.onkeypress(paddle.go_right, "Right")


def exit_restart():
    global game_is_on
    MsgBox = messagebox.askquestion(
        'Breakout', 'Try again?', icon='question')
    if MsgBox == 'yes':
       screen.clear() 
       init_game()
       game_is_on = True
    else:
        screen.close()

init_game()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect  collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() > -280:
        ball.bounce_y()

    #Detect paddle misses
    if ball.ycor() < -280:
        score.life_lost()
        ball.reset_position()
        if score.lifes < 1:
            score.loose()
            game_is_on = False
            exit_restart()

    #Detect collision with wall blocks
    if wall.row_4:
        for block in wall.row_4:
            if block.distance(ball) < 35:
                wall.row_4.remove(block)
                block.hideturtle()
                ball.bounce_y()
                print(len(wall.row_4))
                       
    if wall.row_3:
        for block in wall.row_3:
            if block.distance(ball) < 35:
                wall.row_3.remove(block)
                block.hideturtle()
                ball.bounce_y()

    if wall.row_2:
        for block in wall.row_2:
            if block.distance(ball) < 35:
                wall.row_2.remove(block)
                block.hideturtle()
                ball.bounce_y()

    if wall.row_1:
        for block in wall.row_1:
            if block.distance(ball) < 35:
                wall.row_1.remove(block)
                block.hideturtle()
                ball.bounce_y()
    
    if not wall.row_1 and not wall.row_2 and not wall.row_3 and not wall.row_4:
        score.win()
        game_is_on = False
        exit_restart()

screen.exitonclick()
