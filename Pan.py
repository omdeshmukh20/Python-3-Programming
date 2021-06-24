#Discription: Creating a Pan
#Date: 24/06/21
#Author : Om Deshmukh

class AgeInvalid(Exception):
	def __init__(self,data):
		self.data=data

def main():
	try:
		age=int(input("Enter your age for PAN card"))
		if age<18:
			raise AgeInavlid("your age is less than 18")

	except AgeInvalid as obj:
		print(obj)

	else:
		print("you wil get that PAn card within 7 days")
if __name__ == '__main__':
		main()	
