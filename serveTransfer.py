import socket
import sys
import threading


def createAndTransferFile(connectionSocket,fileNumber):
    f = open(".\probe"+str(fileNumber)+".pdf",'wb') # Open in binary
    data = connectionSocket.recv(1024)
    while(data):
        f.write(data)
        data = connectionSocket.recv(1024)
    f.close()
    connectionSocket.close()

s = socket.socket()
s.bind(("192.168.56.1",8080))
s.listen(3) # Acepta hasta 10 conexiones entrantes.
fileNumber = 0

while(1):
    sc, address = s.accept()
    print(address)

    request = threading.Thread(target = createAndTransferFile,args=(sc,fileNumber,))

    request.start()

    fileNumber = fileNumber + 1

s.close()