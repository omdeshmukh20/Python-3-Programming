#Discription: Even factor program
#Date: 09/07/21
#Author : Om Deshmukh
x = int(input("Enter any number"))
print("The even factors of",x,"are:")
for i in range(2, x + 2):
    if x % i == 0:
            print(i)
