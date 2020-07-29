from socket import *

#Creo el socket para datagramas
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Ato el socket al puerto y la Ip correspondiente
serverSocket.bind(('192.168.56.1',12345))

print ('El servidor is Ready')

while 1:

	message, clientAddress = serverSocket.recvfrom(2048)
	
	messageString = message.decode('utf-8')
	
	if messageString=="1":
		modifiedMessage = bytes('Recibi un 1','utf-8')
	else:
		modifiedMessage = bytes('Recibi algo distinto de 1','utf-8')
	

	serverSocket.sendto(modifiedMessage, clientAddress)
   