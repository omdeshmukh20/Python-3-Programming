#Function Name:PrimeSeries
#Input:20
#Output: 2 3 5 7 11 13 17 19 
#Description:Display Prime Numbers Upto n numbers
#Date: 14/07/2021
#Author: Om Deshmukh


def PrimeSeries(n):
	x=1
	for i in range (2,n):
		if n%i==0:
			x=0
			break
		else:
			x=1
	return x

n=int(input(("Enter Number Upto what Prime Number You Want..?")))
i=2
for i in range (2,n+1):
	if PrimeSeries(i):
		print(i)
	i=i+1


