### Loops ###

# While

my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 2 
else:
    print("Mi condicion es mayor o igual a 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 14:
        print("Se detiene la ejecucion")
        break

    print(my_condition)

# For

my_lists = [35, 25, 53, 15, 38, 33, 62]

for element in my_lists:
    print(element)
    if element == 15:
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi lista ha finalizado")