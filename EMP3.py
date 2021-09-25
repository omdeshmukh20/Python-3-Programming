#Discription:  Python Program To Unpickel Emp Class Objects
#Date: 25/09/21
#Author : Om Deshmukh


import Emp, pickle

# Open The File To Read Objects

f = open('emp.dat', 'rb')

print('Employees Details : ')
while True:
    try:
        # Read Objects From File f
        
        obj = pickle.load(f)
        
        # Display The Contents Of Employee obj
        
        obj.display()
        
    except EOFError:
        
        print('end of file reached...')
        break
    
    # Close The File
    
    f.close()
