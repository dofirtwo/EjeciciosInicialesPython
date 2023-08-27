for x in range(5):
    edad=int(input("Ingrese su edad: "))
    if edad>=80:
        print("su fase de vacunacion contra el covid es: Fase 1")
    elif edad>=70 and edad<80:
        print("su fase de vacunacion contra el covid es: Fase 2")
    elif edad>=60 and edad<70:
        print("su fase de vacunacion contra el covid es: Fase 3")
    elif edad>=30 and edad<60:
        print("su fase de vacunacion contra el covid es: Fase 4")
    elif edad>=18 and edad<30:
        print("su fase de vacunacion contra el covid es: Fase 5")
    elif edad<18:
        print("En espera de Autorización")
    else:
        ("tipo de dato erroneo")