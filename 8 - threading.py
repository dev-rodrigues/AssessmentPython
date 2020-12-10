import threading, time, random

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i    
  return(fat)

def to_list(function, veta, vetb):
  for e in veta:
    vetb.append(function(e))


veta = []
for n in range(0, 1000000):
  veta.append(random.randint(0, 10))

vetb = []
n = 500

size = len(veta)
inicio = time.time()

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

resultado = 0
for n in vetb:
  resultado = resultado + n

print(resultado)