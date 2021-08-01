#Discription: add_sheet is used to create sheet.
#Date: 1/08/21
#Author : Om Deshmukh

# Writing to an excel 
# sheet using Python

import xlwt
from xlwt import Workbook
  
# Workbook is created

wb = Workbook()


# add_sheet is used to create sheet.

sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(1, 0, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA'#Discription: Directory to hold file content and file name.
#Date: 31/07/21
#Author : Om Deshmukh

sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT DEHRADUN')
sheet1.write(0, 2, 'SHASTRADHARA')
sheet1.write(0, 3, 'CLEMEN TOWN')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')
  
wb.save('xlwt example.xls')
