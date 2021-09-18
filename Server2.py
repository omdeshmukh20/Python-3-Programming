#Discription: Create A UDP Server That Sends Messages To The Client
#Date: 18/09/21
#Author : Om Deshmukh



import socket
import time

# Take The Server Name And Port Number

host = 'localhost'
port = 5000

# Create A Socket At Server Side To Use UDP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Let The Server Waits For 5 Seconds

time.sleep(4)

# Send Messages To The Client After Encoding Into Binary String

s.sendto(b"Hello Client, How Are u", (host, port))
msg = "Byee!"
s.sendto(msg.encode(), (host, port))

# Disconnect The Server

s.close()
