#Description - Using the parameeters in function
#Date - 18/07/2021
#Author - Om Deshmukh

#Function accepts nothing and return nothing
def fun():
	print("Function fun")

#function which accpts paramter and returns nothing
def gun(no):
    print("Function gun with parmeter:",no)	

#
def sun(no):
	print("Function sun with parameter:",no)
	return no+1

#function accepts multiple values and returnd multiple values
def AddSub(no1,no2):
	add=no1+no2
	sub=no1-no2
	return add,sub

def main():
	fun()
	gun(11)
	ret=sun(10)
	print("Return value of sun is:",ret)

	ret1,ret2=AddSub(12,10)
	print("Addition is:",ret1)
	print("substraction is:",ret2)

if __name__ == '__main__':
	main()
