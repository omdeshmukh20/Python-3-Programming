#Discription : Accepts File Name From User & Check Whether That file exists In Current Directory Or Not
#Date: 12/09/21
#Author : Om Deshmukh


import os, sys

fname = input("Enter Filename : ")

if os.path.isfile(fname):
    print(fname + " File Exists")
else:
    print(fname + " does not exist")
    sys.exit()
