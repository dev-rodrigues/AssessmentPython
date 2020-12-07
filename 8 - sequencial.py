vet_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fatorial(n):
  fat = n
  for i in range(n-1, 1, -1):
    fat = fat * i
  return(fat)

resultado = 0

for t in vet_a:
  result = fatorial(t)
  resultado = resultado + result

print(result)