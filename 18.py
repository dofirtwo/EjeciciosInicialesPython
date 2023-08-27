x=""
edad=0
nombre=0
estudiantes=[]
while x!="*":
    nombre=input("Ingrese el nombre del estudiante: ").lower()
    edad=int(input("Ingrese la edad del estudiante: "))
    estudiantes.append((nombre,edad))
    x=input("Quiere ingrese (*) si quiere salir, si no ingrese cualquier otro caracter: ")

print()
for n, e in estudiantes:
    if e>=18:
        
        print(f"El estudiante {n} es mayor de edad con {e} años")
    if e>edad:
        edad=e
        nombre=n
print()
print(f"El estudiante mayor del curso es: {nombre} con {edad} años")        
    
        
