lineas = int(input("ingrese un numero:"))
fila = 0
for i in range(1,lineas+1):
    fila +=2
    
    for k in range(i,fila):
        print ("*",end="")
        
    for l in range(fila-2,i-1,-1):
        print ("*",end="")
            
    print() 