#Discription: Factors of (n) number
#Date: 09/07/21
#Author : Om Deshmukh
def factorof(n) :
    i = 1
    while i <= n :
        if (n % i==0):
        	print(i)
        i = i + 1

print("The factors of number are:")
factorof(100)
