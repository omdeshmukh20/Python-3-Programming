#Discription - A Lambda function  to calculate products of elements of a list.
#Date - 19/07/2021
#Author - Om Deshmukh

from functools import *

lst = [1,2,3,4,5]
result = reduce(lambda x,y: x*y, lst)
print(result) 
