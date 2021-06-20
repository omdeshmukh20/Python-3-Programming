#Discription: Inbuikt functin frm modula
#Date: 20/06/21
#Author : Om Deshmukh

#Inbuikt functin frm modula
def Substraction(no1,no2):
	return no1-no2

def SubDecoraor(func_name):
	return func_name(10,5)

def main():
	
	ret=subDecorator(Substraction)

	print("Substraction is",ret)

if __name__ == '__main__':
			main()		
