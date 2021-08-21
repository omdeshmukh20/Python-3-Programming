  

#Discription:  A program to know the effect of any() and all() function
#Date: 19/07/21
#Author : Om Deshmukh

from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])

c=a>b
print("Result of a>b:",c)

print('Check if any one element is true:',any(c))
print('Check if all elements are true:',all(c))
