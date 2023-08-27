pizzaVegetariana=["Pimiento","tofu"]
pizzaNoVegetariana=["Peperoni", "Jamón", "Salmón"]
pizzaFinal=["Tomate", "Mozzarella"]
print("Bienvenido a  pizzería Napolitana elija su tipo de pizza")
print("Pizza Vegetariana")
print("Pizza No Vegetariana")
seleccion = input("Ingrese su seleccion: ").lower()
if seleccion == "pizza no vegetariana":
    print("Ingredientes de la pizza No Vegetariana: ",pizzaNoVegetariana)
    ingredientes = input("Seleccione el Ingrediente que desea en la pizza: ")
    pizzaFinal.append(ingredientes)
elif seleccion == "pizza vegetariana":
    print("Ingredientes de la pizza Vegetariana: ",pizzaVegetariana)
    ingredientes = input("Seleccione el Ingrediente que desea en la pizza: ")
    pizzaFinal.append(ingredientes)
else:
    print("Dato No Valido")

if  seleccion == "pizza no vegetariana" or seleccion == "pizza vegetariana":   
    print("Usted acaba de ordenar una: ",seleccion)
    print("con los siguientes ingredientes:")  
    print(pizzaFinal)