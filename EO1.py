#Discription: Even odd no program.
#Date: 09/08/21
#Author : Om Deshmukh

def even(no):
	if no%2==0:
		print("The num",no,"is even num")
	else:
		print("The num",no,"is a odd num")	


def main():
	no=(int(input("Enter the no")))
	ans=even(no)


if __name__ == '__main__':
	main()
