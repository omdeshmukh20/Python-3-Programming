#Discription: Threading (CPU) Number of CPU cores
#Date: 23/06/21
#Author : Om Deshmukh

import os

def Square(no):
	return no*no

def SerialProcessing():
	arr=range(10)
	ret=[]

	for i in arr:
		ret.append(Square(i))

	print(ret)		

def main():
	print("Inside main")
	print("Number of CPU cores are:",os.cpu_count())

if __name__ == '__main__':
		main()	
