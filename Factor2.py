#Discription: Python Program to find the factors of a number
#Date: 02/08/21
#Author : Om Deshmukh

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)
