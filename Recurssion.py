#Discription: Maximum Recursion limit
#Date: 22/07/21
#Author : Om Deshmukh

def fun():
	i=1
	print(i)
	i=i+1
	fun()

def main():
	fun()

if __name__ == '__main__':
	main()
