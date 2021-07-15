#Discription: Accepting N num and making a list.
#Date: 15/07/21
#Author : Om Deshmukh
def main():
	arr=[]
	print("Enter no of elements")
	size=int(input())

	for i in range(size):
		print("The element no is:",i+1)
		no=int(input())
		arr.append(no)
	

	print("your entered elements are:",arr)	
	print("the sum of ur entered elements is:",sum(arr))
if __name__ == '__main__':
	main()
