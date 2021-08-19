
#Discription:Static Method To Find Square Root Value
#Date: 19/08/21
#Author : Om Deshmukh


import math
class Sample:
    @staticmethod
    def calculate(x):
        result = math.sqrt(x)
        return result
    
# Accept A Number From Keyboard

num = float(input('Enter A Number : '))

# Call The Static Method And Pass num

res = Sample.calculate(num)
print('The Square Root Of {} Is {:.2f}'.format(num, res))
