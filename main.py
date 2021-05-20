from turtle import *
import random
import time
import turtle

screen=Screen()
t=turtle.Turtle()

t.speed(0)
t.penup()
t.color('green')
t.goto(-450,-450)
screen.colormode(255)

def randNumberArr():
    r1=random.randint(0,255)
    r2=random.randint(0,255)
    r3=random.randint(0,255)
    return [r1,r2,r3]

flag=False
for i in range(50):
    for i in range(50):
        arr=randNumberArr()
        t.penup()
        t.fillcolor(arr[0],arr[1],arr[2])
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        t.forward(20)
    flag=not flag
    if(flag==True):
        t.lt(90)
        t.forward(45)
        t.lt(90)
    else:
        t.rt(90)
        t.forward(5)
        t.rt(90)
time.sleep(30)