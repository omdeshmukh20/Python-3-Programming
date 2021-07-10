#Discription: Sum of num in arr
#Date: 10/07/21
#Author : Om Deshmukh
def main():
	arr=[]
	print("Enter the no of elements")
	size=int(input())

	for i in range(size):
		print("The no of element is",i+1)
		no=int(input())
		arr.append(no)

	print("The no of given elements are",arr)
	print("The sum of given elements in arr is",sum(arr))
if __name__=="__main__":
	main()
	
