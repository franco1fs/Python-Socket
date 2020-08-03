import socket
import threading
import sys
import pickle

HEADERSIZE = 5
addr_port = ('192.168.56.1',8080)

socket = socket.create_server(addr_port)

socket.listen(1)

print("server is ready")

def translationMsg(connectionSocket):
    message_header = b''
    message_header = connectionSocket.recv(HEADERSIZE)
    while(len(message_header)>0):
      message_payload = b''
      message_length = int(message_header)
      
      message_payload = connectionSocket.recv(message_length) 
      
      message = pickle.loads(message_payload)
      print("La data es:"+message[1])
      message_header = b''
      message_header = connectionSocket.recv(HEADERSIZE)
    connectionSocket.close()

while 1:
  connectionSocket, addr = socket.accept()

  print(addr)
  
  request = threading.Thread(target = translationMsg,args=(connectionSocket,))

  request.start()
