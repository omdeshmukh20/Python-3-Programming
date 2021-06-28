#Discription: Practice
#Date: 28/06/21
#Author : Om Deshmukh

def Addition(value1,value2):
	return value1+value2

def main():
	print("Enert first no is")
	value1=int(input())

	print("Enert seconf no is")
	value2=int(input())

	ret=Addition(value1,value2)

	print("The addition of two numbers is",ret)

if __name__ == '__main__':
	main()
