#Discription: Python Program To Pickle Emp Class Objects
#Date: 25/09/21
#Author : Om Deshmukh

import Emp, pickle

# Open emp.dat File As A Binary File For Writing

f = open('emp.dat', 'wb')
n = int(input('How Many Employees? '))

for i in range(n):
    id = int(input('Enter Id : ')) 
    name = input('Enter Name : ')
    sal = float(input('Enter Salary : '))
    
    # Create Emp Class Object
    
    e = Emp.Emp(id, name, sal)
    
    # Store The Object e Into The File f
    
    pickle.dump(e, f)
    
# Close The File

f.close()
