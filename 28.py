
def Factorial(n):
    f=1
    for x in range (1,n+1):
        f=f*x
    return f
 
num=int(input("Ingrese un numero: "))
print(Factorial(num))