import time, multiprocessing

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i    
  return(fat)

def to_list(funcao, vetor_a, q):
    vetor_b = []
    for n in vetor_a:
        vetor_b.append(funcao(n))
    q.put(vetor_b)

if __name__ == "__main__":
    veta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vetb = []
    n = 5000
    queue = multiprocessing.Queue()


    tamanho = len(veta)
    time_inicio = time.time()

    p0 = multiprocessing.Process(target = to_list, args = (fatorial, veta[0:int(tamanho / 4)], queue))
    p0.start()

    p1 = multiprocessing.Process(target = to_list, args = (fatorial, veta[int(tamanho / 4): int(tamanho / 2)], queue))
    p1.start()

    p2 = multiprocessing.Process(target = to_list, args = (fatorial, veta[int(tamanho / 2) : int(tamanho * (3 / 4))], queue))
    p2.start()

    p3 = multiprocessing.Process(target = to_list, args = (fatorial, veta[int(tamanho * (3 / 4)) : int(tamanho)], queue))
    p3.start()

    while len(veta) != len(vetb):
        while queue.empty() is False:
            vetb += queue.get()

    p0.join()
    p1.join()
    p2.join()
    p3.join()

    time_fim = time.time()

    sum = 0
    for b in vetb:
        sum = sum + b

    print('resultado: ', sum)