#Discription: Factorial
#Date: 28/06/21
#Author : Om Deshmukh

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % 1 == 0:
       	if x % 2 == 0:
           print(i)
number = 24 


def main():
	print_factors(number)
if __name__ == '__main__':
		main()	
