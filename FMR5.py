#Discription: Filter map reduce
#Date: 13/07/21
#Author : Om Deshmukh
def greater(no):
	if (no>=70) and (no<=90):
		return True
	else:
		return False

def filter(arr):
	brr=[]
	for i in range(len(arr)):
		if greater(arr[i])==True:
			brr.append(arr[i])
	return brr

def map(arr):
	for i in range(len(arr)):
		arr[i]=arr[i]+10

	return arr

def reduce(arr):
	mul=1
	for i in range(len(arr)):
		mul=mul*arr[i]
	return mul				
					 

def main():
	arr=[]
	print("Enter no of elements:")
	value=int(input())

	for i in range(value):
		print("The element no ",i+1," is:")
		no=int(input())
		arr.append(no)


	print("The entered elements are:",arr)	
	newdata=filter(arr)
	print("Elements after filter are:",newdata)

	newdata1=map(newdata)
	print("The elemnts after map are:",newdata1)

	newdata2=reduce(newdata1)
	print("The element after reducing is",newdata2)


if __name__ == '__main__':
			main()	
