import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(('192.168.1.4', 7))
connection.listen(1)
    
while True:
    current_connection, address = connection.accept()
    while True:
        data = current_connection.recv(2048)
        
        data = data.decode('utf-8')
        
        if data == 'stop':
            current_connection.shutdown(1)
            current_connection.close()
            break

        elif data == 'exit':
            current_connection.shutdown(1)
            current_connection.close()
            exit()

        elif data:
            current_connection.send(bytes(data, 'utf-8'))
            print (data)


