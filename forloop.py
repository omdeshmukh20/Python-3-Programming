#Discription: Using for loop
#Date: 14/06/21
#Author : Om Deshmukh

def DisplayF(value):
    print("Output of for loop")
    icnt = 0
    for icnt in range(0,value):
        print("Jay Ganesh")

def DisplayW(value):
    print("Output of while loop")
    icnt = 0
    while icnt < value:
        print("Jay Ganesh")
        icnt = icnt + 1
        
def main():
    print("Enter the number of iterations")
    no = int(input())
    
    DisplayF(no)
    DisplayW(no)
    
if __name__ == "__main__":
    main()
