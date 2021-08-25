#Discription:  Python Program To Accept A Group Of Numbers And Find Their Total Average
#Date: 25/08/21
#Author : Om Deshmukh

def calculate(lst):
    """ To Find Total And Average """
    n = len(lst)
    sum = 0
    for i in lst:
        sum+=i
        avg = sum/n
        return sum, avg
    
# Take A Group Of Integers From Keyboard

print('Enter Number Seprated By Space : ')
lst = [int(x) for x in input().split()]

# Call Calculate () And Pass The List

x, y = calculate(lst)
print('Total : ', x)
print('Average : ', y)
