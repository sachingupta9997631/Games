import turtle
import math
import os
import random

#Creation of Objects
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("lightcyan")
s.bgpic("game.gif")
s.title("Space Bubble - By Sachin")
#

score=0

#Command Prompt Commands
os.system("color b")
os.system("@echo The Rules Of the Game...")
os.system("@echo Your just simply have to touch the Bubbles by using the object")
os.system("@echo press 'a' to turn Left with 90 degree")
os.system("@echo press 'd' to turn Right with 90 degree")
os.system("@echo press 'Up' Arrow to Increase the moving speed of the object")
os.system("@echo press 'Down' Arrow to Decrease the moving speed of the object")
os.system("pause")
#

speed=1
t.speed(0)
t.pensize(3)
t.shape("triangle")
t.color("cyan")
t.penup()
t.setposition(-300,-300)
t.pendown()
for i in range(4):
    t.forward(600)
    t.left(90)

#turtle listen funtions definition
def upspd():
    global speed
    speed+=2

def dnspd():
    global speed
    speed-=2

def left_turn():
    t.left(90)

def right_turn():
    t.right(90)

def iscoll(tur_obj1,tur_obj2):
    d=math.sqrt(pow(tur_obj1.xcor()-tur_obj2.xcor(),2) + pow(tur_obj1.ycor() - tur_obj2.ycor(),2))

    if d<20:
        return True
    else:
        return False
#

turtle.listen()
turtle.onkey(upspd,"Up")
turtle.onkey(dnspd,"Down")
turtle.onkey(left_turn,"a")
turtle.onkey(right_turn,"d")

t.penup()
t.setposition(-305,-305)
t.color("yellow")
t.pendown()
for i in range(4):
    t.forward(610)
    t.left(90)

#Goal of the game
goal_lim=10
goal=[]
for i in range(goal_lim):
    goal.append(turtle.Turtle())
    goal[i].speed(0)
    goal[i].shape("circle")
    goal[i].color("red")
    goal[i].penup()
    goal[i].setposition(random.randint(1,297),random.randint(1,297))

t.penup()
t.setposition(0,0)

#main loop
while True:
    t.forward(speed)
    
    if t.xcor() >295 or t.xcor()<-295:
        t.left(180)
    if t.ycor() >295 or t.ycor()<-295:
        t.right(180)

    for i in range(goal_lim):
        goal[i].forward(3)
    
        if goal[i].xcor()>295 or goal[i].xcor()<-295:
            goal[i].left(45)
        if goal[i].ycor()>295 or goal[i].ycor()<-295:
            goal[i].right(45)
        
        if(iscoll(goal[i],t)):
            goal[i].setposition(random.randint(-290,290),random.randint(-290,290))
            goal[i].left(random.randint(0,360))
            score+=2
            print("\nThe Updated5 Score is: {0}".format(score))
#
