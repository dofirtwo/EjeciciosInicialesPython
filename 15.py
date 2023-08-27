x=""
palabras=[]
while x!="salir":
    x=input("Ingrese una palabra (cuando Termine escriba salir): ").lower()
    palabras.append(x)

palabras.remove("salir")
palabra=palabras
for i in palabras:
    while palabras.count(i)>1:
        palabras.remove(i)
print(palabras)    