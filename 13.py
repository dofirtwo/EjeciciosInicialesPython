edades=[]
for x in range(5):
    edad=int(input("Ingrese la Edad: "))
    edades.append(edad)
min=edades[0]
for x in edades:
    if x<min:
        min=x
print("La edad Menor es: ",min)
max=edades[0]
for x in edades:
    if x>max:
        max=x
print("La edad Mayor es: ",max)