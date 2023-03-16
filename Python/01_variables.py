#Variables

Variable = "Una simple variable"
print(Variable)

otra_variable = "& fea" #esta bariable esta mejor definida, al no tener mayuscula
print(Variable, otra_variable)

my_int_variable= 5
print(Variable, otra_variable, my_int_variable) # concatenacion de variables en un print
print(type(my_int_variable))

todaslasvariables = Variable, otra_variable, my_int_variable
print(todaslasvariables)
print(type(todaslasvariables))

todaslasvariables_str =str(todaslasvariables) #
print(todaslasvariables_str)
print(type(todaslasvariables_str))


#funcines

print(len(todaslasvariables_str))


# Variables en una sola linea

nombre, apellido, edad, alias, ciudad = "Ariel", "Olivo", 23, "AriOli", "Sevilla"
print(alias, edad)
print(nombre, alias, edad)

print("*****************************************")
print("¿Como te llamas?")
nombre_input = input()
print("Hola", nombre_input )
print("¿Cuantos años tienes?")
edad_input = input()
print("con que",edad_input,"vaya un poco viejo para empezar a programar, no?")


