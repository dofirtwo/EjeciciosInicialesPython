import random
lista=[]
for x in range(10):
    lista.append(random.randint(1,100))
lista.sort()
print(lista)