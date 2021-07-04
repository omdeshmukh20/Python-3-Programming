
#Discription : Factor of no
#Date: 4/07/21
#Author : Om Deshmukh
def factor(num):
  factor = [1]
  for i in range(1,num+1):
     if num%i==0:
         factor.append(i)
  return sum(factor)
print(factor(12))
