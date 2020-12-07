import threading

vetorA = [2,3,4,5,6,7,8]
def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i    
  return(fat)

calc = [fatorial(n) for n in vetorA]
t = threading.Thread(target=fatorial, args=[calc])
t.start()