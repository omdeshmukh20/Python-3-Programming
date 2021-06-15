#Discription : Demonstration of selection by function.
#Date: 15/06/21
#Author : Om Deshmukh 

def CheckEven(No):
	if No%2==0:
		return True
	else:
		return False
			
def main():
	print("enter one number")
	value=int(input())

	bret=checkEven(value)

	if bret==True:
		print("{} is Even Number".format(value))
	else:
	    print("{} is odd Number".format(value))	


if __name__ == '__main__':
	main()
