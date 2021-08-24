# Python Program In Which Mercedes Is Sub Class Implements The Abstract Method Of Super Class, Car

#Discription: Python Program In Which Mercedes the Sub Class Implements The Abstract Method Of Super Class, Car
#Date: 24/08/21
#Author : Om Deshmukh

from abstractc2 import Car
class Mercedes(Car):
    def steering(self):
        print('Mercedes Uses Manual And Automatic Steering')
        print('Drive the car')
    
    def breaking(self):
        print('Mercedes Uses Brake Assist System BAS')
        print('Apply Breaks And Stop It')
        
# Create Objects To Mercedes And Use Its Features

m = Mercedes(63)
m.openTank()
m.steering()
m.breaking()
