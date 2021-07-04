#Discription : Factorial
#Date: 4/07/21
#Author : Om Deshmukh
def Factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i

	return(fact)

def main():
	ret=Factorial(5)	

	print("Value of factorial is",ret)

if __name__ == '__main__':
		main()	
