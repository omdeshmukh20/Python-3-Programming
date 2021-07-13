#Discription: Lambda function pos , neg
#Date: 13/07/21
#Author : Om Deshmukh
def main():
	arr=[]
	print("Enter the no of elements:")
	no=int(input())

	for i in range(no):
		print("The element no",i+1,"is:")
		no=int(input())
		arr.append(no)

	pos=0
	neg=0
	zero=0
	neg = len(list(filter(lambda x: (x < 0), arr)))
	pos = len(list(filter(lambda x: (x >= 0), arr)))
	zero = len(list(filter(lambda x: (x == 0 ), arr)))

		
	print("The given numbers are:",arr)	
	
	print("The positive number in arr are:",pos)

	print("The negative number in arr are:",neg)

	print("the zeroth number in arr is",zero)


if __name__ == '__main__':
	main()
