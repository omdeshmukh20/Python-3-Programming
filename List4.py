#Discription: Accept N numbers from user and return addition of that N numbers
#Date: 15/06/21
#Author : Om Deshmukh 

def addition(LIST):
	sum=0
	for i in range(len(LIST)):
		sum=sum+LIST[i]
		return sum	

def main():
	arr=[]
	print("Enter the Number of elements")
	size=int(input())

	for i in range(size):
		print("Enter the element no:",i+1)
		value=int(input())
		arr.append(value)

	print("Accepted data is:",arr)

	ret=Addition(arr)

	print("Addition data is :",ret)

if __name__ == '__main__':
	main()
