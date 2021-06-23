#Discription: Threading (CPU) Serial Processing
#Date: 23/06/21
#Author : Om Deshmukh

import os
import time

def Square(no):
	return no*no

def SerialProcessing():
	start=time.time()
	print("Serial Processing")
	arr=range(100)
	ret=[]

	for i in arr:
		ret.append(Square(i))

	end=time.time()
	print("Time required for serial exicution",end-start)		

def main():
	print("Inside main")
	SerialProcessing()

if __name__ == "__main__":
		main()	
