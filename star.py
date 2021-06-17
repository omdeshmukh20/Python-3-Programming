#Discription: Star Pattern Print
#Date: 17/06/21
#Author : Om Deshmukh

import turtle
turtle.pensize(5)
turtle.speed(20)
turtle.bgcolor("black")

for i in range(8):
	for colours in["yellow","blue","white","green","red","Pink","purple"]:
		turtle.color(colours)
		turtle.color(colours)
		turtle.left(100)
		turtle.left(60)
		turtle.forward(500)

turtle.hideturtle()
