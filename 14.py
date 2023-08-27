x=""
palabras=[]
while x!="salir":
    x=input("Ingrese una palabra (cuando Termine escriba salir): ").lower()
    palabras.append(x)

palabras.remove("salir")
contador=0
palabra=input("Ingrese la palabra para buscar: ").lower()
for i in palabras:
    if i==palabra:
        contador=contador+1
print("la palabra:",palabra,"se repite ",contador," veces")    