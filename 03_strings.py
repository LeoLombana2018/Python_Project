## Strings ##

my_string = "Mi String"
my_other_string = "Mi otro string"

print(len (my_string))
print(len (my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\t Este es un string \nescapado"
print(my_scape_string)

# Formateo
name, surname, age = "Leonardo", "Lombana", 37
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


#Desempaquetado
object = "home"
a, b, c, d = object
print (a)
print (d)

#Division
object_slice = object [1:3]
print(object_slice)

#Reverse
reversed_object = object[::-1]
print(reversed_object)

print(object.capitalize())
print(object.upper())
print(object.count("h"))
print(object.isnumeric())
print(object.lower())
print(object.lower().isupper())
print(object.startswith("m"))
