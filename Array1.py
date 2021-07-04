#Discription : Compairing two array
#Date: 4/07/21
#Author : Om Deshmukh
from numpy import*

a = array([1, 2, 3, 0])
b = array([0, 2, 3, 1])

c = a == b
print('Result Of a == b : ', c)

c = a > b
print('Result Of a == b : ', c)

c = a <= b 
print('Result Of a == b : ', c)
