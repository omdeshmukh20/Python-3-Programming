# Python Program To Handle The ZeroDivisionError Exception

#Discription:  Python Program To Handle The ZeroDivisionError Exception
#Date: 22/08/21
#Author : Om Deshmukh

try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter Two Numbers : ").split()]
    
    c = a/b
    f.write("Writing %d Into myfile" %c)
    
except ZeroDivisionError:
    print('Division By Zero Happened')
    print('Please Do Not Enter 0 In Input')
    
finally:
    f.close()
    print('File Is Closed')
