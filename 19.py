
temperaturas=[]
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
promedio=[]
for d in dias:
    dia=d
    mayor=float(input(f"Ingrese la temperatura mayor del {d}: "))
    menor=float(input(f"Ingrese la temperatura menor del {d}: "))
    d=dias[0]
    temperaturas.append((dia, mayor, menor))
       
BuscarTemp=float(input("Ingrese la temperatura que quiera buscar: "))    
verificacion=False 
for d,m, n in temperaturas:
    operacion = (m+n)/2
    dia=d
    promedio.append((dia,operacion))
    if BuscarTemp==m:
        BuscarTemp=m,dia
        print(BuscarTemp)
        verificacion=True
    
if verificacion==False:
    print("NO EXISTE")
    
for o in promedio:
    print(o)

    