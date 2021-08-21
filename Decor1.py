
#Discription: A decorator to increase the value of function by 2.
#Date: 21/08/21
#Author : Om Deshmukh

def decor(fun):
	def inner():
		value = fun()
		return value+2
	return inner
	
def num():
    return 10

result_fun = decor(num)
print(result_fun())  
