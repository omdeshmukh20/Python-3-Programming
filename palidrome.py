#Discription - checking the string is palidrom or not
#Date: 05/09/21
#Author : Om Deshmukh

def palidrome(num):
    x=num[::-1]
    if(x==num):
        print("Palidrome")
    else:
        print("Not a Palidrome ")
palidrome("madam ")
