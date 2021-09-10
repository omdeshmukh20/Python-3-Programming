#Discription: Accepts File Name From User & Check Whether That File Exists In Current Directory Or Not
#Date: 10/09/21
#Author : Om Deshmukh


import os, sys

fname = input("Enter Filename : ")

if os.path.isfile(fname):
    print(fname + " File Exists")
else:
    print(fname + " does not exist")
    sys.exit()
