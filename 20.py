from datetime import datetime
año=datetime.now()
x=0
num=0
cuenta=[]
while x!=7:
    print("1. Crear Cuenta")
    print("2. Consignar Cuenta")
    print("3. Retirar Cuenta")
    print("4. Consultar Cuenta Por Código")
    print("5. Consultar Cuenta por Identificación Cliente")
    print("6. Listar Cuentas")
    print("7. Salir")
    x=int(input("Ingrese Opción (1-7): "))
    
    if x == 1:
        identificacion=int(input("Ingrese la identificacion: "))
        nombre=input("Ingrese su nombre: ")
        correo=input("ingrese su Correo: ")
        num=num+1
        saldo=0
        fecha=año.strftime("%d/%m/%Y")
        codigo=(f"{año.year}-{num}")
        cuenta.append([identificacion,nombre,correo,codigo,saldo])
        
    if x == 2:     
        confirmacion=input("Ingrese el codigo de la cuenta: ")
        for i in cuenta:
            contador1=cuenta.index(i)
            if confirmacion==i[3]:
                elementos=0            
                for x in cuenta:
                    elementos +=len(x)                     
                fecha=[año.strftime("%d/%m/%Y")]
                saldo=int(input(f"usted tiene {i[4]} de saldo. Ingrese el saldo que desea agregar a la cuenta: "))
                datos=[saldo,fecha]
                cuenta[contador1][4]+=saldo             
                if elementos==5:
                    cuenta[contador1].extend(fecha)
                    break
                elif elementos==6:
                    cuenta[contador1][5]=fecha
                    break
            elif confirmacion!=i[3]:
                print("El codigo ingresado no coincide con ninguna cuenta de ahorros")
                break
                
    if x == 3:     
        confirmacion=input("Ingrese el codigo de la cuenta: ")     
        for i in cuenta:
            contador1=cuenta.index(i)            
            if confirmacion==i[3] and i[4]>0:   
                retiro=int(input(f"usted tiene {i[4]} de saldo. Igrese la cantidad que desea retirar: "))
                saldo=saldo-retiro
                cuenta[contador1][4]=saldo
                break
            else:
                print("No hay Saldo en la cuenta")
                
    if x == 4:     
        confirmacion=input("Ingrese el codigo de la cuenta: ")
        for i in cuenta:
            if confirmacion==i[3]:   
                print(i)
                break
            
    if x == 5:     
        confirmacion=int(input("Ingrese la identificacion de la cuenta: "))
        for i in cuenta:
            if confirmacion==i[0]:   
                print(i)
                break
            
    if x == 6:     
        for i in cuenta:
                print(i)
                
print("Vuelva Pronto :D")