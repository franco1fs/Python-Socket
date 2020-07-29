from socket import *

serverName = '192.168.56.1'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Ingrese un String: ')

clientSocket.sendto(bytes(message,'utf-8'), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print ('Recibido del servidor:', modifiedMessage.decode('utf-8'))

clientSocket.close()