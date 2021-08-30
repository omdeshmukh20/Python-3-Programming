#Discription: Accept N Numbers From User,
#                (Filter) The Number In 70 To 90, (Map) Then Add 10 In Each Number, (Reduce) Multiply Them
#Date: 30/08/21
#Author : Om Deshmukh
#Function Name : Number_Between(), Adding_Number(), Product_Number()

from functools import*

def Number_Between(iNo):
    x = 70
    y = 91

    if iNo in range(x, y):
        return True
    else:
        return False

def Adding_Number(no):
    return no + 10

def Product_Number(no1, no2):
    return no1 * no2


def main():

    arr = []

    size = int(input("Enter Number Of Elements : "))

    for i in range(size):

        iNo = i + 1
        iNo = int(input("Enter Numbers : "))
        arr.append(iNo)

    print("Your Entered Data Is : ", arr)

    Filtering = list(filter(Number_Between, arr)) 
    print("After Filter From 70 To 90 Is : ", Filtering)    

    Mapping = list(map(Adding_Number, Filtering))
    print("After Adding 10 In Each : ", Mapping)

    Reducing = reduce(Product_Number, Mapping)
    print("Product Of The Number Is : ", Reducing)    
    

if __name__ == "__main__":
    main()
