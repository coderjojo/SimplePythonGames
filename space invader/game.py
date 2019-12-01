# import turtle

import turtle
import random
import math
import os
from os import sys


# set up screen
obj = turtle.Screen()
obj.bgcolor('red')
obj.title('Space Invaders')
obj.bgpic('pro.gif')
obj.register_shape('alien.gif')
obj.register_shape('spaceship.gif')
# add border

from tkinter import *


class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('black')
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()

        for draw in range(4):
            self.forward(600)
            self.left(90)
        # create score


class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.goto(-290, 302)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write('Score: {}'.format(self.score), False, align='left', font=('Arial', 14, 'normal'))

    def change_score(self, points):
        self.score += points
        self.update_score()

    #def play_sound(self):
        #winsound.PlaySound('sound.wav', winsound.SND_ASYNC)


# Create player
class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color('green')
        self.shape('circle')
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # border Checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('classic')
        self.color('blue')
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        # border Checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def slowspeed(self):
        self.speed -= 1


def isCollision(t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a * a) + (b * b))

    if distance < 20:
        return True
    else:
        return False


player = Player()
border = Border()
border.draw_border()
game = Game()
goals = []
for count in range(6):
    goals.append(Goal())
# set keyboard bindings

turtle.listen()
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.increasespeed, 'Up')
turtle.onkey(player.slowspeed, 'Down')

# speed up the game

obj.tracer(3)

# main loop
while True:
    obj.update()
    player.move()

    for goal in goals:
        goal.move()

        if isCollision(player, goal):
            goal.jump()
            game.change_score(10)
            #game.play_sound()
