#Discription: Python Program to find Largest of Two Numbers
#Date: 03/08/21
#Author : Om Deshmukh

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

if(a > b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")
