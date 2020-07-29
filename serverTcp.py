import socket
import threading
addr_port = ('192.168.56.1',8080)

socket = socket.create_server(addr_port)

socket.listen(1)

print("server is ready")

def translationMsg(connectionSocket):
    sentence = connectionSocket.recv(1054)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

while 1:
    connectionSocket, addr = socket.accept()

    request = threading.Thread(target = translationMsg,args=(connectionSocket,))

    request.start()