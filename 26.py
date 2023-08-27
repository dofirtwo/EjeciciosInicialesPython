numeros=[2,3,5,5,1,32,5,7,8]
pares=[]
impares=[]
def Orden(n):
    for x in n:
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
Orden(numeros)
print("Numeros Pares: ")
for P in pares:
    print(P)
print("Numeros Impares:")
for I in impares:
    print(I)