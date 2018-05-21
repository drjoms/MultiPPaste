#!/usr/bin/python3           # This is server.py file
import socket
import subprocess
subprocess.run(["clear"])
# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket._LOCALHOST
host = '0.0.0.0'

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

   # print("Got a connection from %s" % str(addr))
   #print ("asic chat?")
    msg = 'Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('UTF-8'))
    incmes = clientsocket.recv(1024)
    print(incmes.decode('utf-8'))
    clientsocket.close()



