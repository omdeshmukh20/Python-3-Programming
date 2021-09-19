#Discription: a program which accept number from user and return the count of digits in between 3 and 7.
#Date: 19/09/21
#Author : Om Deshmukh

def Dig(no):
    cnt=0
    if no < 0:
        no=-(no)

    while no > 0:
        idigit=int(no%10)
        if idigit>2 and idigit<7:
            cnt=cnt+1
        no=int(no/10)

    return cnt

def main():
    num=int(input("Enter the number :"))
    ret=Dig(num)
    print("The count of digit betwn 3 and 7 is :",ret)


if __name__=="__main__":
    main()  
