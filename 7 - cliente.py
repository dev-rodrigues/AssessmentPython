import pickle, time, socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname()

destiny = (host_name, 8080)

try:
    for i in range(0, 5):
        socket_client.sendto(' '.encode('utf-8'), destiny)
        ok = False
        bytes = []
        try:
            bytes = socket_client.recv(1024)
            response = pickle.loads(bytes)
            print(response)
            ok = True
        except:
            print('falhou ao obter, tentativa: ', i + 1)

        if ok:
            break
        time.sleep(10)
except Exception as erro:
    print('erro', str(erro))