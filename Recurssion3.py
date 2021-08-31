#Discription: Accept N Number From User To Print Same Number In Form Of * Using Recursion 
#Date: 31/08/21
#Author : Om Deshmukh

def Recursion_Pattern(iNo): 
    
    if iNo >= 1:
        no = iNo - 1
        print(end = "* ")
        Recursion_Pattern(no) # Calling Itself And Then Return The Value To Function Call

def main():

    value = int(input("Enter Number To Print * : "))
    Recursion_Pattern(value) # Function Call

if __name__ == "__main__":
    main()
