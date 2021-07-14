#Function Name:EvenBetween
#Input:10  20
#Output:10 12 14 16 18
#Description:Display Even Numbers in between range
#Date: 14/07/2021
#Author: Om Deshmukh



m=int(input("Enter Starting Number"))
n=int(input("Enter Ending Number"))

if m>n:
	print("Not Valid..!")
elif n>m:
	while m<=n:
		if(m%2==0):
		   print(m)
		else:
			print()
		m=m+1