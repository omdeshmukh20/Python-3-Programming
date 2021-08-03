#Discription: Python Program to Check Leap Year using Elif Statement
#Date: 03/08/21
#Author : Om Deshmukh

year = int(input("Please Enter the Year Number you wish: "))

if (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):
          print("%d is Not the Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not the Leap Year" %year)
