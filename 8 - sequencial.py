import random
vet_a = []
def fatorial(n):
  fat = n
  for i in range(n-1, 1, -1):
    fat = fat * i
  return(fat)
resultado = 0
for n in range(0, 1000000):
  vet_a.append(random.randint(0, 10))
for t in vet_a:
  result = fatorial(t)
  resultado = resultado + result
print(resultado)