#Function Name:CompareArray
#Input:--

#Output:
#Result of arr=brr [False False  True False]
#Result of arr>=brr [False False  True  True]

#Description:Compare Arrays Between two Arrays
#Date: 14/07/2021
#Author: Om Deshmukh

from numpy import *

arr=array([10,20,50,60])
brr=array([30,40,50,10])

ans=arr==brr
print("Result of arr=brr",ans)

ans=arr>=brr
print("Result of arr>=brr",ans)
