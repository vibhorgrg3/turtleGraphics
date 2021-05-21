from turtle import *
import random
import time
import turtle

screen=Screen()
t=turtle.Turtle()

t.speed(0)
# t.penup()
# t.color('green')
# t.goto(-450,-450)
screen.colormode(255)

def randNumberArr():
    r1=random.randint(0,255)
    r2=random.randint(0,255)
    r3=random.randint(0,255)
    return [r1,r2,r3]

flag=False
t.pensize(10)
# randno=random.randint(1-10)*90
def randomWalk(t):
    for i in range(500):
        arr=randNumberArr()
        t.lt(random.randint(1,10)*90)
        t.color(arr[0],arr[1],arr[2])
        t.forward(random.randint(20,100))
    # if(flag==True):
    #     t.lt(90)
    #     t.forward(45)
    #     t.lt(90)
    # else:
    #     t.rt(90)
    #     t.forward(5)
    #     t.rt(90)
randomWalk(t)



time.sleep(30)
