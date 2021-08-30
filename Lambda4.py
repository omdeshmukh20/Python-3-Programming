#Discription: Accept N Numbers From User And Display Power Of 2 Using Lambda Function
#Date: 30/08/21
#Author : Om Deshmukh

def main():
    
    value = int(input("Enter The Number : "))

    iRet = list(map(lambda no: 2 ** no, range(value + 1)))

    for i in range(1, value + 1):
        print("Power Of(x^2)",i, "Is", iRet[i])
   

if __name__ == "__main__":
    main()
