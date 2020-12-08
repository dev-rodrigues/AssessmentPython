import time, threading, multiprocessing

veta = [5000, 5000, 5000, 4, 500, 600, 7, 8, 100000, 99999]

inicio_sequencial = time.time()

def fatorial(n):
  fat = n
  for i in range(n-1, 1, -1):
    fat = fat * i
  return(fat)

resultado = 0
for t in veta:
  result = fatorial(t)
  resultado = resultado + result

fim_sequencial = time.time()

print('inicio medicao sequencial: ', inicio_sequencial)
print('fim medicao sequencial: ', fim_sequencial)
print('tempo gasto: ', fim_sequencial - inicio_sequencial)

####################################################################################################################
def to_list(function, veta, vetb):
  for e in veta:
    vetb.append(function(e))

vetb = []
n = 500

size = len(veta)
inicio = time.time()

inicio_threading = time.time()

threading0 = threading.Thread(target = to_list, args = (fatorial, veta[0:int(size / 4)], vetb))
threading0.start()

threading1 = threading.Thread(target = to_list, args = (fatorial, veta[int(size / 4): int(size / 2)], vetb))
threading1.start()

threading2 = threading.Thread(target = to_list, args = (fatorial, veta[int(size / 2) : int(size * (3 / 4))], vetb))
threading2.start()

threading3 = threading.Thread(target = to_list, args = (fatorial, veta[int(size * (3 / 4)) : int(size)], vetb))
threading3.start()

threading0.join()
threading1.join()
threading2.join()
threading3.join()

fim_threading = time.time()

print('\n')

print('inicio medicao threading: ', inicio_threading)
print('fim medicao threading: ', fim_threading)
print('tempo gasto: ', fim_threading - inicio_threading)

####################################################################################################################

def to_list_(funcao, vetor_a, q):
    vetor_b = []
    for n in vetor_a:
        vetor_b.append(funcao(n))
    q.put(vetor_b)

processing_inicio = time.time()

if __name__ == "__main__":
    veta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vetb = []
    n = 5000
    queue = multiprocessing.Queue()


    tamanho = len(veta)
    

    p0 = multiprocessing.Process(target = to_list_, args = (fatorial, veta[0:int(tamanho / 4)], queue))
    p0.start()

    p1 = multiprocessing.Process(target = to_list_, args = (fatorial, veta[int(tamanho / 4): int(tamanho / 2)], queue))
    p1.start()

    p2 = multiprocessing.Process(target = to_list_, args = (fatorial, veta[int(tamanho / 2) : int(tamanho * (3 / 4))], queue))
    p2.start()

    p3 = multiprocessing.Process(target = to_list_, args = (fatorial, veta[int(tamanho * (3 / 4)) : int(tamanho)], queue))
    p3.start()

    while len(veta) != len(vetb):
        while queue.empty() is False:
            vetb += queue.get()

    p0.join()
    p1.join()
    p2.join()
    p3.join()

processing_fim = time.time()

print('\n')

tempo = float(processing_fim - processing_inicio)

print('inicio medicao processing: ', processing_inicio)
print('fim medicao processing: ', processing_fim)
print('tempo gasto: ', tempo )


    