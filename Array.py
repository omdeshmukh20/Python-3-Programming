#Discription: Type , Range , length of an array
#Date: 26/06/21
#Author : Om Deshmukh

from array import*

def main():

	arr=array('i',[11,1,51,101,111,121])

	print(type(arr))
	print(len(arr))
	print(arr[0])

	for i in range(len(arr)):
		print(arr[i])

	icnt=0
	while icnt<len(arr):
		print(arr[icnt])
		icnt+=icnt+1	

if __name__=="__main__":
	main()
