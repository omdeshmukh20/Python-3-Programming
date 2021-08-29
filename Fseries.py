#Discription: Fibnocii series
#Date: 29/08/21
#Author : Om Deshmukh

def fibo(n):
    a=0
    b=1
    print(a,"\n")
    print(b,"\n")
    for x in range(n-2):
        c=a+b
        print(c,"\n")
        a=b
        b=c
    return c
num=int(input("Enter the number "))
fibo(num)
