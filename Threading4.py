#Discription:#Discription: Multiprocessing (CPU) 
#Date: 23/06/21
#Author : Om Deshmukh

import os
import time
import multiprocessing

def Square(no):
	return no*no

def ParallelProcessing():
	start=time.time()
	print("Parallel Processing")
	arr=range(1000000)
	
	pobj=multiprocessing.Pool()

	ret=pobj.map(Square,arr)

	end=time.time()
	print("Time required to parallel exicution",end-start)

	for i in arr:
		ret.append(Square(i))

	end=time.time()
	print("Time required for parallel exicution",end-start)

def SerialProcessing():
	start=time.time()
	print("Serial Processing")
	arr=range(1000000)
	ret=[]

	for i in arr:
		ret.append(Square(i))

	end=time.time()
	print("Time required for serial exicution",end-start)		

def main():
	print("Inside main")
	SerialProcessing()
	ParallelProcessing()

if __name__ == "__main__":
		main()	
