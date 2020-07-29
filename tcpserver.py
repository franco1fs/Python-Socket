from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('192.168.1.4',7))

serverSocket.listen(1)

print('El servidor está Listo...')



while 1:
	
	connectionSocket, addr = serverSocket.accept()
	
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
    
    