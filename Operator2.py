#Discription: init method..
#Date: 25/06/21
#Author : Om Deshmukh

class Student():
	def __init__(self,str,a,b,c):
		self.name=str
		self.m1=a
		self.m2=b
		self.m3=c


def main():
	obj1=Student("Om",56,86,78)
	obj2=Student("Piyush",90,50,45)

	if obj1==obj2:
		print("Both the students are same")
	else:
		print("Both the student are different")	


if __name__ == '__main__':
	main()
