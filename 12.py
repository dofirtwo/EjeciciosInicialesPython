x=0
while x!=4:
    print("MENÚ DE OPCIONES")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    x=int(input("Ingrese Opción: "))
    if x==1:
        print("ESTA EN LA OPCION 1")
        print("Para regresar al menu principal ingrese (salir)")
        salir=input().lower()
    if x==2:
        print("ESTA EN LA OPCION 2")
        print("Para regresar al menu principal ingrese (salir)")
        salir=input().lower()
    if x==3:
        print("ESTA EN LA OPCION 3")
        print("Para regresar al menu principal ingrese (salir)")
        salir=input().lower()
print("Vueva Pronto")