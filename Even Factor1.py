#Discription: A program which accept number from user and print even factors of that  number.  
#Date: 23/08/21
#Author : Om Deshmukh


def Factors(no):

    if(no<=0):
        return

    for i in range(1,no):
        if no%i==0 and i%2==0:
            print(i,end=" ")


def main():
    x=int(input("Enter the number :"))
    Factors(x)

if __name__=="__main__":
    main()   
