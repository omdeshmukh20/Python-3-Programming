#Discription: Open A File And Read Data From It
#Date: 16/09/21
#Author : Om Deshmukh


with open('sample.txt', 'r') as f:
    for line in f:
        print(line)
