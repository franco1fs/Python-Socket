from socket import *

serverName = '192.168.1.4'
serverPort = 7

clientSocket = socket(AF_INET, SOCK_STREAM)



clientSocket.connect((serverName,serverPort))
sentence = ''

while (sentence!='exit' and sentence!='stop'):

    sentence = input('Ingrese un string : ')

    clientSocket.send(bytes(sentence, 'utf-8'))

    modifiedMessage = clientSocket.recv(1024)

    print ('Recibido del servidor: ', modifiedMessage.decode('utf-8'))

clientSocket.close()

