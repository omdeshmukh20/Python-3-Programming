#Discription: Accept File Name From User & Open That File & Display The Contents Of That File On Screen
#Date: 10/09/21
#Author : Om Deshmukh


def main():

    name = input("Enter the file name that you want to Read : ")
    
    fobj = open(name,"r")   # create new file
    
    print("Data from file is : \n")
    print(fobj.read())
    
if __name__ == "__main__":
    main()
