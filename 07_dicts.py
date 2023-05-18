### Dictionaries ###
my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre":"Leonardo", "Apellido":"Lombana", "Edad":38, 1:"Python"}

my_dict = {
    "Nombre":"Leonardo", 
    "Apellido":"Lombana", 
    "Edad":38, 
    "Languages":{"Python", "Swift", "JS"},
    1:1.67
    }
print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])

my_dict["Barrio"] = "Patio Bonito"
print(my_dict)

del my_dict["Barrio"]
print(my_dict)

print("Leonardo" in my_dict)
print("Apellido" in my_dict)

print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())