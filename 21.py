import math
x=0
def AreaCirculo(R):
    Area=math.pi*(R*R)    
    return Area
def AreaTriangulo(B,A):
    Area=(B*A)/2    
    return Area
def AreaCuadrado(L):
    Area=L*L    
    return Area
while x!=4:
    print("1. area Circulo")
    print("2. area Triangulo")
    print("3. area Cuadrado")
    print("4. Salir")
    x=int(input("Ingrese Opción (1-4): "))
    if x==1:
        r=float(input("Ingrese El Radio del Cirulo: "))
        print(f"el area es: {AreaCirculo(r)}")
        print()
    if x==2:
        b=float(input("Ingrese la Base del Triangulo: "))
        a=float(input("Ingrese la Altura del Triangulo: "))
        print(f"el area es: {AreaTriangulo(b,a)}")
        print()
    if x==3:
        l=float(input("Ingrese El lado del Cuadrado: "))
        print(f"el area es: {AreaCuadrado(l)}")
        print()
print()
print("Vuelva Pronto :D")