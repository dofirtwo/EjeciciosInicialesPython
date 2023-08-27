num=int(input("ingrese un numero: "))
for n in range(2, num):
    if num % n == 0:
        print("No es primo")
        break
    else:
        print("Es primo")
        break

