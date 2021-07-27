#Discription: Printing max num from arr
#Date: 27/07/21
#Author : Om Deshmukh

def main():
	arr=[]
	size=int(input("Enter the size of array"))
	for i in range(size):
		arr.append(int(input()))
	print("Data is : ",arr)
	print("Maximum number is : ",max(arr))	


if __name__ == '__main__':
		main()	
