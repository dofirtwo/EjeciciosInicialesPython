nombresGrupoA=[]
sexosGrupoA=[]
nombresGrupoB=[]
sexosGrupoB=[]
for x in range(3):
    nombre=input("ingrese su nombre: ")
    sexo=input("ingrese su sexo(Fememino o Masculino): ").upper()
    if nombre < "m" and sexo == "FEMENINO":
        nombresGrupoA.append(nombre)
        sexosGrupoA.append(sexo)
        
    elif nombre > "n" and sexo == "MASCULINO":
        nombresGrupoA.append(nombre)
        sexosGrupoA.append(sexo)
    
    elif nombre > "m" or nombre<"n":
        nombresGrupoB.append(nombre)
        sexosGrupoB.append(sexo)
    
print("GRUPO A")
print(nombresGrupoA,sexosGrupoA)

print("GRUPO B") 
print(nombresGrupoB,sexosGrupoB)