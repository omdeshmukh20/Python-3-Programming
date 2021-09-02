#Discription : Accept N Number From User And Find The Factorial Using Recursion 
#Date: 2/09/21
#Author : Om Deshmukh

def Recursion_Factorial(iNo):

    if(iNo == 0):
        return 1
    return iNo * Recursion_Factorial(iNo - 1)

def main():

    value = int(input("Enter The Number : "))
    iRet = Recursion_Factorial(value)
    
    print("Factorial Of {} Is {} ".format(value, iRet)) 

if __name__ == "__main__":
    main()
