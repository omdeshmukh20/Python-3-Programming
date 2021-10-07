#Description:Implementations of AnyAll
#Date: 07/10/2021
#Author: Om Deshmukh


from numpy import *

arr=array([10,20,50,60])
brr=array([30,40,50,10])

c=arr<brr
print("Result of arr>brr is",c)

print("Check if one of Condition is True:",any(c))
print("Check if all of Condition is True:",all(c))
