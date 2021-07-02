
#Discription :Add,sub,mul,div
#Date: 2/07/21
#Author : Om Deshmukh
def add(value1,value2):
	add=value1+value2
	return(add)

def sub(value1,value2):
	sub=value1-value2
	return(sub)

def mul(value1,value2):
  	mul=value1*value2
  	return(mul)

def div(value1,value2):
	div=value1/value2	
	return (div)

def main():
	
	ret1=add(11,2)
	ret2=sub(11,2)
	ret3=mul(11,2)
	ret4=div(11,2)

	print("Addition is",ret1)
	print("Substraction",ret2)
	print("Multiplication is",ret3)
	print("Dividion is",ret4)                
if __name__ == '__main__':
		main()	
