import socket
import sys

serverName = '192.168.56.1'
serverPort = 8080

clientSocket = socket.socket()

clientSocket.connect((serverName,serverPort))

f = open ("Python_ características y concurrencia.pdf", "rb")
l = f.read(1024)

while (l):
    clientSocket.send(l)
    l = f.read(1024)
f.close()
clientSocket.close()