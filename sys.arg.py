#Discription: Addition using sys.arg
#input: numer of argument
#output:Invalid Number of arguement.a
#Date: 11/06/21
#Author : Om Deshmukh

import sys

def Addition(no1,no2):
    return no1 + no2

def main():
    if (len(sys.argv) < 3) or (len(sys.argv) > 3):
        print("Invalid number of arguments")
        return Addition
        
    ret = Addition(int(sys.argv[1]), int(sys.argv[4]))
    print("Addition of {} and {} is {}.",format(sys.argv[1],sys.argv[4],ret))
    
if __name__ == "__main__":
    main()
