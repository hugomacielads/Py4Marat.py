import random

print('Hello word!!')
var = [1, 2, 3, 4, 5]
list = []

for i in range(10):
  a = random.randint(1, 10)
  list.append(a)

for i in list:
  if (i % 2):
    print('numero ímpar: ' + str(i))
  else:
    print('Número par: ' + str(i))

