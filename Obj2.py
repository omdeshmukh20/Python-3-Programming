#Discription: Addition and substractio of function.
#Date: 21/07/21
#Author : Om Deshmukh

def Add(no1,no2):
	return no1+no2

def Sub(no1,no2):
	return no1-no2

def main():
	print("Enter first no")
	value1=int(input())
	print("Enter second no")
	value2=int(input())

	ret=Add(value,value2)
	print("Addition is:",ret)

	ret=Sub(value1,value2)
	print("Substraction is:",ret)

	if __name__ == '__main__':
		main()
