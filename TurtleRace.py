from turtle import *
from random import randint
from time import sleep

Red = Turtle()
Orange = Turtle()
Yellow = Turtle()
Green = Turtle()
Blue = Turtle()
Indigo = Turtle()
Violet = Turtle()

TurtleScore = Turtle()
TurtleScore.ht()



def Start():
    global Red, Orange, Yellow, Green, Blue, Indigo, Violet
    Speed = 3
    #Red
    #Red = Turtle()
    Red.shape("turtle")
    Red.pencolor("Red")
    Red.fillcolor("Red")
    Red.st()
    Red.width(3)
    Red.speed(Speed)

    Red.penup()
    Red.setpos(-150, -200) #450
    Red.seth(90)
    Red.pendown()

    #Orange
    #Orange = Turtle()
    Orange.shape("turtle")
    Orange.pencolor("Orange")
    Orange.fillcolor("Orange")
    Orange.st()
    Orange.width(3)
    Orange.speed(Speed)

    Orange.penup()
    Orange.setpos(-100, -200) #450
    Orange.seth(90)
    Orange.pendown()

    #Yellow
    #Yellow = Turtle()
    Yellow.shape("turtle")
    Yellow.pencolor("Yellow")
    Yellow.fillcolor("Yellow")
    Yellow.st()
    Yellow.width(3)
    Yellow.speed(Speed)

    Yellow.penup()
    Yellow.setpos(-50, -200) #450
    Yellow.seth(90)
    Yellow.pendown()

    #Green
    #Green = Turtle()
    Green.shape("turtle")
    Green.pencolor("Green")
    Green.fillcolor("Green")
    Green.st()
    Green.width(3)
    Green.speed(Speed)

    Green.penup()
    Green.setpos(0, -200) #450
    Green.seth(90)
    Green.pendown()

    #Blue
    #Blue = Turtle()
    Blue.shape("turtle")
    Blue.pencolor("Blue")
    Blue.fillcolor("Blue")
    Blue.st()
    Blue.width(3)
    Blue.speed(Speed)

    Blue.penup()
    Blue.setpos(50, -200) #450
    Blue.seth(90)
    Blue.pendown()

    #Indigo
    #Indigo = Turtle()
    Indigo.shape("turtle")
    Indigo.pencolor("Indigo")
    Indigo.fillcolor("Indigo")
    Indigo.st()
    Indigo.width(3)
    Indigo.speed(Speed)

    Indigo.penup()
    Indigo.setpos(100, -200) #450
    Indigo.seth(90)
    Indigo.pendown()
    
    #Violet
    #Violet = Turtle()
    Violet.shape("turtle")
    Violet.pencolor("Violet")
    Violet.fillcolor("Violet")
    Violet.st()
    Violet.width(3)
    Violet.speed(Speed)

    Violet.penup()
    Violet.setpos(150, -200) #450
    Violet.seth(90)
    Violet.pendown()

def Reset():
    Red.reset()

    #Orange.clear()
    Orange.reset()

    #Yellow.clear()
    Yellow.reset()

    #Green.clear()
    Green.reset()

    #Blue.clear()
    Blue.reset()

    #Indigo.clear()
    Indigo.reset()

    #Violet.clear()
    Violet.reset()

def Hide():
    Red.ht()
    Orange.ht()
    Yellow.ht()
    Green.ht()
    Blue.ht()
    Indigo.ht()
    Violet.ht()

def Show():
    Red.st()
    Orange.st()
    Yellow.st()
    Green.st()
    Blue.st()
    Indigo.st()
    Violet.st()



    Reset()
    Hide()
    sleep(.5)
    Start()

Hide()

rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
Score = [0 for x in range(len(rainbow))]

def win():
    Reset()
    TurtleScore.reset()
    TurtleScore.ht()
    Hide()
    sleep(.5)
    Start()
    writeScore()

def writeScore():
    style = ('Courier', 15, 'italic')
    for x in range(7):
        TurtleScore.pencolor(rainbow[x])
        TurtleScore.fillcolor(rainbow[x])
        TurtleScore.penup()
        TurtleScore.goto(-150 + (50 * x), -240)
        TurtleScore.pendown()
        TurtleScore.write(Score[x], font=style, align='center')

#setup
colormode(255)

screen = Screen()
setup(500, 500)
title("Turtle Race")

#1st prep
Start()
writeScore()

while True:
    Red.fd(randint(1,10))
    Orange.fd(randint(1,10))
    Yellow.fd(randint(1,10))
    Green.fd(randint(1,10))
    Blue.fd(randint(1,10))
    Indigo.fd(randint(1,10))
    Violet.fd(randint(1,10))

    if(Red.ycor() >= 199):
        Score[0] += 1
        win()
    elif(Orange.ycor() >= 199):
        Score[1] += 1
        win()
    elif(Yellow.ycor() >= 199):
        Score[2] += 1
        win()
    elif(Green.ycor() >= 199):
        Score[3] += 1
        win()
    elif(Blue.ycor() >= 199):
        Score[4] += 1
        win()
    elif(Indigo.ycor() >= 199):
        Score[5] += 1
        win()
    elif(Violet.ycor() >= 199):
        Score[6] += 1
        win()