#Discription: Accept File Name & One String From User & Return The Frequency Of That String From File
#Date: 12/09/21
#Author : Om Deshmukh



import sys
import os.path

def main():

    if len(sys.argv) < 2 :
        print("please give filename using command line")
        exit()

    if os.path.exists(sys.argv[1]):
        print("file exist")
    else:
        print("file does not exist")

    file_name = sys.argv[1]
    char = input("Enter word to be searched:")
    ch = 0

    with open(file_name, 'r') as c:
        for line in c:
            char2 = line.split()
            for i in char2:
                if (i == char):
                    ch = ch + 1
    print("Occurrences of the word:")
    print(ch)
    
    c.close()

if __name__=="__main__":
    main()
