from socket import *
import datetime
import threading
import time

def handle_request(socket, data, client_address):
    messageString = data.decode('utf-8')
    messageString += 'Recibi lo anterior y te respondo'
    response = bytes(messageString, 'utf-8')
    print('Procece me duermo 10 seg')
    time.sleep(10)
    socket.sendto(response, clientAddress)    
    print('Ya mande la respuesta')

# Creo el socket para datagramas
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Ato el socket al puerto e IP
serverSocket.bind(('192.168.1.4', 12345))

print ('El servidor is reaady')

while 1:
    
    message, clientAddress = serverSocket.recvfrom(2048)

    print('Recibi conexion abro thread')
    c_thread = threading.Thread(target = handle_request, args = (serverSocket, message, clientAddress))
    c_thread.daemon = True
    c_thread.start()