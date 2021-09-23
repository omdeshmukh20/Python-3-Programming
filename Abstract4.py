#Discription: Python Program In Which RollsRoyce Sub Class Implements The Abstract Methods Of The Super Class, Car.
#Date: 24/08/21
#Author : Om Deshmukh

from abstractc2 import Car
class RollsRoyce(Car):
    
    def steering(self):
        print('RollsRoyce')
        print('Drive The Car')
        
    def breaking(self):
        print('RollsRoyce Uses Authomatc Breaks')
        print('Apply Breaks And Stop It')
        
# Create Objects To RollsRoyce And Use Its Features

s = RollsRoyce(9030)
s.openTank()
s.steering()
s.breaking()
