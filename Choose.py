#Discription: the choosen appears in arr
#Date: 11/07/21
#Author : Om Deshmukh
def main():
	drr=[]
	print("Enter the number of elements:")
	no=int(input())

	for i in range(no):
		print("The number of element is:",i+1)
		no=int(input())
		drr.append(no)

	print("Entered number of elements is:",drr)
	print("Element you want to choose is:")
	no=int(input())

	print("The choosen element appears",drr.count(no))

if __name__ == '__main__':
	main()
