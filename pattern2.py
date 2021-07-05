#Discription :pattern printing
#Date: 5/07/21
#Author : Om Deshmukh
def figure(n):
	#Outer loop
	for i in range(0,n):

		for j in range(0,i+1):

			print("*",end="")

		print("")

figure(5)
