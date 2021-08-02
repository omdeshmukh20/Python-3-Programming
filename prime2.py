# All prime number in an interval. Number should be greater than 1
#Date: 02/08/21
#Author : Om Deshmukh

start = 11
end = 25
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
