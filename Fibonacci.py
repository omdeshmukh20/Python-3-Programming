#Function Name:Fibonacci
#Input:7
#Output:1 1 2 3 5 8  
#Description:Display Fibonacci Series upto n numbers
#Date: 26/08/2021
#Author:Om Deshmukh


n=int(input("upto which u want Number"))
a=b=1
print(a)
print(b)
for i in range(1,n-1):
	c=a+b
	print(c)
	a=b
	b=c
