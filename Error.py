#Discription: Error example
#Date: 07/09/21
#Author : Om Deshmukh

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()
