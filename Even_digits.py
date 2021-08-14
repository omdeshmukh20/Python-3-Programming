#Discription:Accept Digit From User And Find How Many Numbers Are Even In That Digit
#Date: 1/08/21
#Author : Om Deshmukh

# Even_Digits Operation


def Even_Digits(iValue1):

    iDigit = 0
    iCnt = 0

    if iValue1 < 0:
        iValue1 =- iValue1

    if iValue1 <= 0:
        exit("Invalid Input!")

    while iValue1 > 0:

        iDigit = iValue1 % 10
        if iDigit % 2 == 0:
            iCnt += 1
        iValue1 = iValue1 // 10

    return iCnt

# Entry Point 

def main():

    iNo1 = int(input("Enter The Number : "))

    iRet = Even_Digits(iNo1)

    print("Number Of Even Digits From {0} Is : {1}".format(iNo1, iRet))

# Code Starter

if __name__ == "__main__":
    main()
