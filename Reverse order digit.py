#Discription: Accept Digit From User And Display That Number Separately In Reverse Order
#Date: 12/09/21
#Author : Om Deshmukh




# Display_Digits Operation


def Display_Digits(iValue1):

    if iValue1 <= 0:
        iValue1 =- iValue1

    iDigit = 0

    while iValue1 > 0:

        iDigit = iValue1 % 10
        print(iDigit)
        iValue1 = iValue1 // 10


# Entry Point 

def main():

    iDigit = int(input("Enter The Digits : "))

    Display_Digits(iDigit)

# Code Starter

if __name__ == "__main__":
    main()
