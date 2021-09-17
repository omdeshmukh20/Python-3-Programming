#Function Name:AreaCircle..
#Input: 5..
#Output:Area of Circle is 78.53981633974483
#       Area of Circle is 78.54
#Description:Calculates Area of Circle
#Date: 10/07/2021
#Author: Shubham Lodha

import math

r=float(input("Enter Radius"))
ans=float(math.pi*r*r)

print("Area of Circle is",ans);
print("Area of Circle is {:0.2f}".format(ans))
