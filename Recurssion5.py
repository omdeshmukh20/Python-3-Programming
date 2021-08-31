#Discription:Accept N Number From User And Print That Number In Reverse Order Using Recursion 
#Date: 31/08/21
#Author : Om Deshmukh

def Recursion_Number_Printing(iNo):
    
    if (iNo > 0): 
        print(iNo, end = ' ') 
        Recursion_Number_Printing(iNo - 1) 
    
    '''if iNo > 0:
        print(iNo, end = " ")
        iNo = iNo - 1
        Recursion(iNo)
    '''

def main():

    value = int(input("Enter One Number : "))

    Recursion_Number_Printing(value)

if __name__ == "__main__":
    main()
