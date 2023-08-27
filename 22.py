def catidadPalabra(C,P):
    Repetidos=C.count(P)
    return Repetidos
cadena=input("Ingrese el texto: ")
if not cadena:
    print("Ingrese un texto")
else:
    palabra=input("Ingrese la palabra que desea buscar del texto: ").lower()    
    print(f"{catidadPalabra(cadena,palabra)}")    