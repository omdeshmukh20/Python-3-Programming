#Discription:Check whether the number is armstrong or not
#Date: 05/09/21
#Author : Om Deshmukh

num=int(input("Enter the num "))
sum=0
temp=num
x=len(str(num))
while(temp>0):
    r=temp%10
    sum=sum+r**x
    temp=temp//10
if(num==sum):
    print("Armstrong number ")
else:
    print("Not a Armstrong number")
