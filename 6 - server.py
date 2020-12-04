import os, socket, pickle

class Archive:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def to_map(self):
        return {
            'name': self.name
        ,   'size': self.size
    }

def get_arquives(directory):


    archives = []

    archives_aux = os.listdir(directory)

    for archive in archives_aux:
        path = str(directory + archive)
        if os.path.isfile(path):            
            size = os.stat(path).st_size
            archive = Archive(path, size)
            archives.append(archive.to_map())

    return archives

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
server_port = 8080

socket_server.bind((host_name, server_port))
socket_server.listen()

print(host_name, 'waiting connection in port ', server_port)

while True:
    (socket_client, addr) = socket_server.accept()

    print('server ', host_name, ' connected with ', addr)

    request = socket_client.recv(1024)

    request_decoded = request.decode('utf-8')

    response = get_arquives(request_decoded)
    response_encoded = pickle.dumps(response)

    socket_client.send(response_encoded)

    socket_client.close()
    break