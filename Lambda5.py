#Discription: Accept N Numbers From User And Multiply The Number Using Lambda Function 
#Date: 30/08/21
#Author : Om Deshmukh

def main():

    Mult = lambda iNo1, iNo2 : iNo1 * iNo2

    value1 = int(input("Enter First Number For Multiply : "))

    value2 = int(input("Enter Second Number For Multiply : "))

    ret = Mult(value1, value2)
    print("Multiplication Of {} And {} Is {} ".format(value1, value2, ret))

if __name__ == "__main__":
    main()
