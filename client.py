#!/usr/bin/python3           # This is client.py file

#note to self:
#implement -c flag, so pipe from app to copy paste client could be used
#multiline
#GUI/kivi
#SSL


import socket
import sys



try:
        str(sys.argv[1])
        host = str(sys.argv[1])
except:
    print('it failed')
    host = input('IP address/Domain Name  of machine where to connect?')


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = '192.168.0.227'
#host = input('Ip address of machine where to connect?')

port = 9999
# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)
user_input = input ('what do yo want to insert?\n ')
s.send(user_input.encode('UTF-8'))
s.close()
print (msg.decode('UTF-8'))



