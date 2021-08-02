#Discription: Program to find all even numbers. 
#Date: 02/08/21
#Author : Om Deshmukh

def gun(no):
	for i in range(2,no+1,2):
		print(i)

def main():
	no=int(input("Enter the no"))
	gun(no)


if __name__ == '__main__':
	main()
