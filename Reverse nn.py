#Discription: Python Program to Print Natural Numbers in Reverse Order
#Date: 03/08/21
#Author : Om Deshmukh
 
number = int(input("Please Enter any Number: "))
i = number

print("List of Natural Numbers from {0} to 1 in Reverse Order : ".format(number)) 

while ( i >= 1):
    print (i, end = '  ')
    i = i - 1
