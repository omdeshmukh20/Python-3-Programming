def Pattern(no):
    for i in range(0,no+1,1):
        for j in range(1,no+1,1):
            if(i>=j):
                print(j,end=" ")
        print("")

def main():
    no1=int(input("Enter Number"))
    Pattern(no1)

if __name__=="__main__":
    main()
