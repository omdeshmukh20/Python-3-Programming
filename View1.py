#Discription: Create A View Of An Existing Array. 
#Date: 16/09/21
#Author : Om Deshmukh



from numpy import*

a = arange (1, 6) # It Create Elements From 1 To 5
b = a.view() # Create a View Of a And Call It b

print('Original Array : ', a)
print('Newly Array : ', b)
print("\n")


b[0] = 99 # Modify oth Element Of b With The Value 99

print('After Modification Replace 0th Value With 99 : ')
print("\n")

print('Original Array : ', a)
print('Newly Array : ', b)
print("\n")
