import socket

serverName = '192.168.56.1'
serverPort = 8080

clientSocket = socket.socket()

clientSocket.connect((serverName,serverPort))

sentence = input("ingrese un string")

clientSocket.send(bytes(sentence,'utf-8'))

modifiedMsg = clientSocket.recv(1024)

print("recibido del servidor",modifiedMsg.decode('utf-8'))

clientSocket.close()