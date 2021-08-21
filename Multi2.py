#Discription:# A program to understand how a function return multiple value
#Date: 21/08/21
#Author : Om Deshmukh



def sum(a,b):
    c=a+b
    d=a-b
    return c,d


x,y=sum(10,5)
print("Addition is :",x)
print("Substraction is :",y)   
