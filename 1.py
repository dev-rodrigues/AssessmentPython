import psutil, threading, time

from psutil import Process

cache = {
    'processes': []
}

class Process:
    def __init__(self, pid, name, use_cpu, use_memory):
        self.pid = pid
        self.name = name
        self.use_cpu = use_cpu
        self.use_memory = use_memory
    
    def to_map(self):

        return {
                'pid': self.pid
            ,   'name': self.name
            ,   'use_cpu': self.use_cpu
            ,   'use_memory': self.use_memory
        }

def get_processo():
    pids = psutil.pids()

    collected_processes = []

    for pid in pids:
        try:
            name = psutil.Process(pid).name()
            memory = format(psutil.Process(pid).memory_percent(), '.2f')
            cpu = psutil.Process(pid).cpu_percent()
            process = Process(pid, name, cpu, memory)
            collected_processes.append(process)
        except:
            pass

    cache['processes'].clear()
    cache['processes'].append(collected_processes)


class ThreadProcess(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.id = threadID
        self.name_process = name
        self.counter = counter
    
    def run(self):
        while True:
            get_processo()

t_process = ThreadProcess(1, 'GET-PROCESS', 1)
t_process.start()

processes = ''

while processes == '':
    try:
        processes = cache['processes'][len(cache['processes']) - 1]
    except:
        print('[LOADING]\n')
        time.sleep(10)

for p in processes:
    print(p.to_map(), '\n')


