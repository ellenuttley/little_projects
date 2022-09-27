from turtle import *

pu()
goto(-350, 400)
speed(7)
bgcolor('grey')
width(5)



def blacksquare():
        color("grey", "black")
        begin_fill()
        for sides in range(4):
            pd()
            fd(100)
            rt(90)
        end_fill()

def whitesquare():
    color("grey", "white")
    begin_fill()
    for sides in range(4):
        pd()
        fd(100)
        rt(90)
    end_fill()

def row():
    for squares in range(3):
        blacksquare()
        fd(100)
        whitesquare()
        fd(100)

def linebreak_one():
    pu()
    rt(90)
    fd(100)
    rt(90)
    fd(550)
    rt(180)

def linebreak_two():
    pu()
    rt(90)
    fd(100)
    rt(90)
    fd(650)
    rt(180)

def pattern():
    for line in range(4):
        row()
        linebreak_one()
        row()
        linebreak_two()


pattern()