#Discription:Iterative approach
#Date: 14/06/21
#Author : Om Deshmukh

#Iterative aproach
def StartDynamic(NO,Message="Jay Ganesh"):
	iCnt=0
	while iCnt<NO:
		print(message)
		iCnt=iCnt+1

def main():
	print("Enter number of times you want to display message on screen")
	value=int(input())
	print("Enter the message")
	name=input()


	StartDynamic(value,name)
	
	StartDynamic(value)

if __name__ == '__main__':
		main()	
