# Variables

my_variable = 'My String variable en python'
print(my_variable)

my_int_variable = 8
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)
print()

#Concatenacion de variables en un print
print (my_variable, my_int_variable, my_bool_variable, my_int_to_str_variable)
print("Este es le valor de mi variable boolean:", my_bool_variable)
print()

#Funciones del sistema
print(len(my_int_to_str_variable))
print(len(my_variable))
print()

#Variables en una sola linea
name, surname, age = "Leonardo", "Lombana", 37
print("Mi nombre es:" ,name, "Mi apellido es:" ,surname, "Mi edad es:" ,age)
