#Discription: Straight , Reverse Threading
#Date: 24/06/21
#Author : Om Deshmukh

import threading

def straight():
    for i in range(51):
        print(i)
def reverse():
    for i in range(50,-1,-1):
        print(i)

def main():
    thread1=threading.Thread(target=straight,args=())
    thread2=threading.Thread(target=reverse,args=())

    thread1.start()
    thread1.join()
    thread2.start()

if __name__ == '__main__':
    main()



     
