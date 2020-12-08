import psutil, socket
import pickle, threading
import time

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host_name = socket.gethostname()

socket_server.bind((host_name, 8080))
print('Aguardando conexão na porta: ', host_name,':', 8080)

cache = {
    'memory': []
}

class Memory:
    def __init__(self, total, used):
        self.total = total
        self.used = used
    
    def to_map(self):
        return {
            'total': self.total,
            'used': self.used
        }

def collect_memory_information(memory):
    total_memory = memory.total
    used_memory = memory.used
    collected_memory = Memory(total_memory, used_memory)

    cache['memory'].append(collected_memory)

def get_last_info_of_memory():
    last = len(cache['memory']) - 1
    response = cache['memory'][last]
    return response

class ThreadMemoria(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        while True:
            print ("starting: " + self.name)
            memory = psutil.virtual_memory()
            collect_memory_information(memory)
            print ("sleeping...")            
            time.sleep(10)

thread = ThreadMemoria(1, 'ThreadMemoria', 1)
thread.start()

while True:
    response = None

    (request, client) = socket_server.recvfrom(1024)

    if request.decode('utf-8') == 'close':
        break

    if len(cache['memory']) > 0:
        response = get_last_info_of_memory()

        bytes_response = pickle.dumps(response.to_map())
        socket_server.sendto(bytes_response, client)

socket_server.close()