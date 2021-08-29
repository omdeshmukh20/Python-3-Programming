#Discription: Leap year or not
#Date: 29/08/21
#Author : Om Deshmukh

year=int (input("Enter the year "))
if(year%400==0) or (year%4==0):
    print("Leap Year")
elif(year%100==0):
    print("Not a Leap Year ")
else:
    print("Not a Leap Year")
