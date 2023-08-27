salario=int(input("ingrese su salario: "))
int(salario)
if salario >= 12000000 and salario <= 15000000:
    impuesto3=salario/3*100
    print("impuesto que debe pagar es: ",impuesto3)
    
elif salario >= 15000000 and salario <= 20000000:
    impuesto5=salario/5*100
    print("impuesto que debe pagar es: ",impuesto5)
    
elif salario >=20000000 and salario <= 30000000:
    impuesto8=salario/8*100
    print("impuesto que debe pagar es: ",impuesto8)
    
elif salario > 30000000:
    impuesto10=salario/10*100
    print("impuesto que debe pagar es: ",impuesto10)
    
else:
    print("Valor fuera de rango")
