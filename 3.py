edad=int(input("ingrese su edad: "))
if edad <=5:
    print("El valor de su entrada es GRATIS")
    
elif edad>5 and edad<18:
    print("El valor de su entrada es de $5000 pesos")
    
elif edad>=18:
    print("El valor de su entrada es de $10000 pesos")