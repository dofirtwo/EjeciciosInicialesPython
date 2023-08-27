def calcularIva(p, i=0.19):
    return p * (1 + i)
precio=int(input("Ingrese el precio del producto: "))
iva=int(input("Igrese el iva (ejemplo de como agregar: 0.13): "))
print(calcularIva(precio,iva))