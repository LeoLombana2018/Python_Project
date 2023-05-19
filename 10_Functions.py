### Functions ###

def my_function():
    print("Esto es una funcion")

my_function()

#################################

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(6,5)

##################################

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum
my_result = sum_two_values_with_return(2,8)
print(my_result)

##################################

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Leonardo", "Lombana")


