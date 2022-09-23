'''
#TODO fix drawBox penUp ==> autonomous, needs to be shorter
#TODO fix circle 2 spawning in the middle and than move to right need to spawn in the right position

'''

import turtle
from turtle import *
import time

class Canvas:
    def __init__(self, color):
        self.color = color
        self.width = width
        bgcolor(self.color)

class Box:
    def __init__(self,color, width, positionX, positionY, rotation, forward):
        self.color = color
        self.width = width
        self.positionX = positionX
        self.positionY = positionY
        self.rotation = rotation
        self.forward = forward

    def drawBox(self):
        pen = turtle.Turtle()
        pen.color(self.color)
        pen.width(self.width)
        pen.hideturtle()
        pen.penup()
        pen.goto(self.positionX, self.positionY)
        pen.pendown()
        pen.fd(60)
        pen.rt(self.rotation)
        pen.fd(self.forward)
        pen.rt(self.rotation)
        pen.fd(60) #  forward2 ??
        pen.rt(self.rotation)
        pen.fd(self.forward)

class Circle:
    def __init__(self, color, shape, positionX, positionY):
        self.color = color
        self.shape = shape
        self.positionX = positionX
        self.positionY = positionY

    def drawCircle(self):
        light = turtle.Turtle()
        light.shape(self.shape)
        light.color(self.color)
        light.penup()
        light.goto(self.positionX, self.positionY)




def normalize():
    redLight = cirlceR.drawCircle()
    redLight

    time.sleep(2)
    cirlceBR = Circle("black", "circle", 0, 40)
    cirlceBR.drawCircle()
    greenLight = cirlceG.drawCircle()
    greenLight

    time.sleep(4)
    cirlceBG = Circle("black", "circle", 0, -40)
    cirlceBG.drawCircle()
    orangeLight = cirlceO.drawCircle()
    orangeLight

    time.sleep(1)
    cirlceBO = Circle("black", "circle", 0, 0)
    cirlceBO.drawCircle()

    redLight = cirlceR.drawCircle()
    redLight

def flicker():
    cirlceO2 = Circle("orange","circle",-150, 0)
    orangeLight2 = cirlceO2.drawCircle()
    orangeLight2
    # print("On")
    time.sleep(2)
    # print("Off")
    cirlceB2 = Circle("black", "circle", -150,0)
    blackLight2 = cirlceB2.drawCircle()
    blackLight2
    time.sleep(2)


#Create a turtle object
screen = turtle.Screen()
screen.title("TrafficLight-Simulation")
screen.listen()

canvasBg = Canvas("black")
boxOutline = Box("yellow", 3, -30, 60, 90, 120)
boxOutline2 = Box("yellow", 3, -180, 60, 90, 120)


cirlceR = Circle("red","circle",0 , 40)
cirlceO = Circle("orange","circle",0, 0)
cirlceB = Circle("black", "circle", 0,0)
cirlceG = Circle("green","circle",0, -40)

cirlceR2 = Circle("red","circle",-150 , 40)
cirlceO2 = Circle("orange","circle",-150, -150)
cirlceB2 = Circle("black", "circle", -150,-150)
cirlceG2 = Circle("green","circle",-150 , -40)

box = boxOutline.drawBox()
box2 = boxOutline2.drawBox()

# redLight2 = cirlceR2.drawCircle()
orangeLight2 = cirlceO2.drawCircle()
blackLight2 = cirlceB2.drawCircle()
# greenLight2 = cirlceG2.drawCircle()




# redLight = cirlceR.drawCircle()
# orangeLight = cirlceO.drawCircle()
# blackLight = cirlceB.drawCircle()
# greenLight = cirlceG.drawCircle()

state = True

while state:
    # normalize()
    flicker()

#Normal Sequense
'''
while True:
    redLight = cirlceR.drawCircle()

    time.sleep(2)
    cirlceBR = Circle("black", "circle", 0, 40)
    cirlceBR.drawCircle()
    greenLight = cirlceG.drawCircle()

    time.sleep(4)
    cirlceBG = Circle("black", "circle", 0, -40)
    cirlceBG.drawCircle()
    orangeLight = cirlceO.drawCircle()

    time.sleep(1)
    cirlceBO = Circle("black", "circle", 0, 0)
    cirlceBO.drawCircle()

    redLight = cirlceR.drawCircle()
'''
#Flicker
'''
while True:
    orangeL = cirlceOrange.drawCircle()
    print("On")
    time.sleep(2)
    print("Off")
    blackL = cirlceBlack.drawCircle()
    time.sleep(2)
'''



done()
