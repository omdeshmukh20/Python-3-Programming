#Discription: Create A TCP/IP Server Program That Sends Messages To A Client
#Date: 18/09/21
#Author : Om Deshmukh


import socket

# Take The Server Name And Port Number

host = 'localhost'
port = 3000

# Create A Socket At Server Side Using TCP/IP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind The Socket With Server And Port Number

s.bind((host, port))

# Allow Maximum 1 Connection To The Socket 

s.listen(1)

# Wait Till A Client Accepts Connection

c, addr = s.accept()

# Display Client Address

print("Connection From : ", str(addr))

# Send Messages To The Client After Encoding Into Binary String

c.send(b"Hello Client, How Are You")
msg = "Byee!"
c.send(msg.encode())

# Disconnect The Server

c.close()
