# Python Program To Create A Car Abstract Class That Conatins An Instance Variable, 
# A Concrete Method And Two Abstract mMethods

#Discription:  Python Program To Create A Car Abstract Class That Conatins An Instance Variable
#Date: 24/08/21
#Author : Om Deshmukh

from abc import*
class Car(ABC):
    def __init__(self, regno):
        self.regno = regno
        
    def openTank(self):
        print('Fill The Fuel Into The Tank')
        print('For The Car With Rengo', self.regno)
        
    @abstractmethod
    def steering(self):
        pass
    
    @abstractmethod
    def breaking(self):
        pass
