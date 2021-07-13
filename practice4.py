#Discription: Vowel or not
#Date: 13/07/21
#Author : Om Deshmukh
def main():
    print("The element is:")
    ch=input()

    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
        or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ele,"Is a vowel")
    else:
        print(ch,"Is not a vowel")    

if __name__ == '__main__':
        main() 
