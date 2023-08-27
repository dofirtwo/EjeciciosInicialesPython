
numeros=[2,3,5,5,1,32,5,7,8]
def sumaLista(nL):
    suma=0
    for x in nL:
        num=x
        suma=suma+num
    return suma
print(sumaLista(numeros))