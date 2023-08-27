
def triangulo(L1,L2,L3):
    if (L1+L2)>L3:
        if (L1+L3)>L2:
            if (L2+L3)>L1:
                if ((L1*L1)+(L2*L2))==(L3*L3):
                    Forma=True
                else:
                    Forma=False                   
    else:
        Forma=False      
    return Forma

lado1=int(input("Ingrese el primer lado del Trigualo: "))
lado2=int(input("Ingrese el Segundo lado del Trigualo: "))
lado3=int(input("Ingrese el Tercer lado del Trigualo: "))
Forma=triangulo(lado1,lado2,lado3)

if Forma == True:
    print("Es un Triangulo Rectangulo, FELICIDADES :D")
elif Forma == False:
    print("NO ES UN TRIANGULO")
