num1=int(input("Igrese el primer Numero: "))
num2=int(input("Igrese el segundo Numero: "))
for multiplo in range(num1,num2):
    if(multiplo % 3 == 0):
        print(multiplo)