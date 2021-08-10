#Discription: Addition of 2 numbers
#Date: 10/08/21
#Author : Om Deshmukh

def add(no1,no2):
	add=no1+no2
	return add

def main():
	no1=int(input("Enter the number"))
	no2=int(input("Enter the number"))
	print("The entered numbers are",no1,"and",no2)
	Ans=add(no1,no2)

	print("The addition is",Ans)

if __name__ == '__main__':
		main()	
