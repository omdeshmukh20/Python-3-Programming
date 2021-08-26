#Function Name:BubbleSort
#Input: 5 (10 50 90 -5 0)

#Output: Sorted Array is [-5,0,10,50,90]

#Description:Bubble-Sort  
#Date: 26/08/2021
#Author: Om Deshmukh



from array import *
x=array('i',[])
print("Enter How Many Elements..?",end='')
n=int(input())

for i in range (n):
	print("Enter Elements:",end='')
	x.append(int(input()))
print("Original Array:",x)

#Bubble Sort
for i in range(n-1):
	for j in range(n-1-i):
		if x[j]>x[j+1]:
			t=x[j]
			x[j]=x[j+1]
			x[j+1]=t

print("Sorted Array is:",x)
