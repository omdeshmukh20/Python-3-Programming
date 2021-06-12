#Discription: Types of function definations in arguements
#input:Imports
#output: inside fun, inside gun
#Date: 11/06/21
#Author : Om Deshmukh

#positional arguement
def Student(name,rno,address,marks):
	print("Name is:",name)
	print("Roll n is:",rno)
	print("Address is:",address)
	print("Marks is:",marks)

#Keyword Arguements
def Computer(RAM,Processor,HDD):
	print("RAM size is",RAM)
	print("Processor nme is",Processor)
	print("Size of HDD is",HDD)

#default Arguement(Should br from Right to Left order)
def CicleArea(Radious,PI=3.14):
	print("Value of PI is",PI)
	return PI* Radious* Radious

#Variable number of arguements
def Fun(*Value):
	print("number of arguemnts are:",len(Value))


def main():
	Student("Om",12,"Walvekar Nagar",100)
	
	Computer(Processor="i7",RAM=8,HDD="1TB")
	Computer(RAM=16,HDD="512GB",Processor="i5")
	
	CicleArea(10.25)
	CicleArea(Radious=10.25,PI=7.25)
	
	Fun(10,20,30)
	Fun(11,21,51,101,152)
	Fun()

if __name__ == '__main__':
	main()
