#Discription: List of pets using if else
#Date: 06/09/21
#Author : Om Deshmukh 
  
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
