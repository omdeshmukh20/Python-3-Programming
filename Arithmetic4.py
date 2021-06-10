#Discription: Substraction of two numbers using function
#input: From user
#output: Expected to user
#Date: 10/06/21
#Author : Om Deshmukh

def Substraction(value1, value2):
    ret=value1 - value2
    return ret

def main():    
    no1=int(input("Enter first number"))
    no2=int(input("enter second number"))
    ans=Substraction(no1,no2)
    print("Substraction is",ans)

    no1=int(input("Enter first number"))
    no2=int(input("enter second number"))
    ans=Substraction(no1,no2)
    print("Substraction is",ans)

if __name__ == '__main__':
    main()
