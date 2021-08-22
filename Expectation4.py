

#Discription:  Python Program To Handle IO Error Produced By Open() Function.
#Date: 22/08/21
#Author : Om Deshmukh

try:
    name = input('Enter Filename : ')
    f = open(name, 'r')
    
except IOError:
    print('File Not Found : ', name)
    
else:
    n = len(f.readlines())
    print(name, 'has', n, 'lines')
    f.close()
    
