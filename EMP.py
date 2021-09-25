#Discription:  Python Program To Create An Emp Class With Employee Details As Instance Variable
#Date: 25/09/21
#Author : Om Deshmukh


class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))
