import calendar

def dias(a, m):
    return calendar.monthrange(a, m)[1]

año=int(input("Ingrese el año: "))
mes=int(input("Ingrese el mes (1-12): "))

print("El mes",mes,"del año",año,"Tiene",dias(año,mes),"dias")