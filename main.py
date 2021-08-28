import random

print('Hello word!!')
# var = [1, 2, 3, 4, 5]
list = []

listPar = []
listImpar = []
cont = 0

while cont <= 20:
  for i in range(100):
    a = random.randint(1, 20)
    if a in list:
      continue
    else:
      #a = a ** 2
      list.append(a)
      cont += cont + 1

list.sort()

for i in list:
  if (i % 2):
    print('numero ímpar: ' + str(i))
    listImpar.append(i)
  else:
    print('Número par: ' + str(i))
    listPar.append(i)

print("\nLista aleatória de números pares", listPar)
print("Lista aleatória de números ímpares", listImpar)