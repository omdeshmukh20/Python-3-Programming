#Discription : No is prime or not
#Date: 4/07/21
#Author : Om Deshmukh
num=5
conditon=False

if num>1:
	for i in range(2,num):
		if num%i==0:
			conditon=True

if conditon:
	print(num,"is not a prime number")
else:
	print(num,"is a prime number")
