import socket
import pickle

serverName = '192.168.56.1'
serverPort = 8080
HEADERSIZE = 5

clientSocket = socket.socket()

clientSocket.connect((serverName,serverPort))
sentence = "1"
while(sentence!=""):
    sentence = input("ingrese un string")

    dictionary = {1:sentence}
    msg = pickle.dumps(dictionary)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)

    clientSocket.send(msg)


clientSocket.close()