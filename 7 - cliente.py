import psutil, socket
import pickle, threading
import time

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host_name = socket.gethostname()
server_port = 8080

destiny = (host_name, server_port)