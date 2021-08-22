

#Discription: Python Program To Handle Syntax Error Given By eval() Function
#Date: 22/08/21
#Author : Om Deshmukh

try:
    date = eval(input("Enter Date : "))
    
except SyntaxError:
    print("Invalid Date Entered")
    
else:
    print("You Entered : ", date)
    
