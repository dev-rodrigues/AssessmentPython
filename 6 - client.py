import os, socket, pickle

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_client.connect((socket.gethostname(), 8080))

    directory = input('put the path')
    
    socket_client.send(directory.encode('utf-8'))

    response = socket_client.recv(1024)
    response_decoded = pickle.loads(response)

    print(response_decoded)

    socket_client.close()

except  Exception as erro:
    print(str(erro))