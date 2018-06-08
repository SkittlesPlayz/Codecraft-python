from turtle import *
shape("arrow")
def changeSize():                   
    size = input("What would you like to change the size to? - ")
    pensize(size)
    print("Pen size changed to " + str(size))
def changeAngle():
    angle = input("What would you like to change the angle to? - ")
    right(angle)
    print("Turned " + str(angle) + " degrees")
def move():
    move = input("How far would you like to move? RETARD - ")
    forward(move)
    print("Moved" + str(move)+ " spaces")

while True:
    changeSize()
    changeAngle()
    move()

