#Discription:  a program which accept number from user and display its multiplication of 
#Date: 23/08/21
#Author : Om Deshmukh

def Factor(no):
    mult=1
    if no <= 0:
        return

    for i in range(1,no):
        if no%i==0:
            mult=mult*i   

    return mult

def main():
    x=int(input("Enter the number :"))
    ret=Factor(x)
    print("The output is :",ret)             


if __name__=="__main__":
    main() 
