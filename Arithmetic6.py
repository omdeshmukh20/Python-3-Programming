#Discription: Multiplication of two numbers using function
#input: From user
#output: Expected to user
#Date: 10/06/21
#Author : Om Deshmukh

def Multiplication(value1, value2):
    ret=value1*value2
    return ret

def main():    
    no1=int(input("Enter first number"))
    no2=int(input("Enter second number"))
    ans=Multiplication(no1,no2)
    print("additon is",ans)

    no1=int(input("Enter first number"))
    no2=int(input("enter second number"))
    ans=Multiplication(no1,no2)
    print("Multiplication is",ans)

if __name__ == "__main__":
        main()    
