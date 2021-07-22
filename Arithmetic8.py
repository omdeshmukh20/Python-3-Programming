#Discription: Addition and Substraction in constructor
#Date: 22/07/21
#Author : Om Deshmukh

class Arithematic:          #defination of class
	value=111


	def __init__(self,i,j):         #class constructor                                                                                                                                                           
		print("Inside Constructor")
		self.no1=i               # class instance variable  
		self.no2=j

	def Add(self):
		return self.no1+self.no2

	def Sub(self):
		return self.no1-self.no2	


def main():
	obj1=Arithematic(21,11)
	obj2=Arithematic(101,51)

	ret=obj1.Add();
	print("Addition is",ret)
	ret=obj1.Sub()
	print("Substration is",ret)

	ret=obj1.Add()
	print("Addition is",ret)
	ret=obj1.Sub()
	print("Substration is",ret)

		

if __name__ == '__main__':
		main()	
