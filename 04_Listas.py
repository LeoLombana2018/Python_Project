### Listas ###
my_lists = list()
my_other_list = []

print (len(my_lists))

my_lists = [35, 25, 53, 15, 38, 33, 62]
print(my_lists)
print(len(my_lists))

my_other_list = [38, 1.67, "September", "Leonardo", "Lombana"]
print(my_other_list)

print(type(my_other_list))
print(my_other_list[1])
print(my_other_list[3])
print(my_other_list[-4])

print(len(my_other_list))
print(my_other_list.count(38))

age, heigth, month_born, name, surname = my_other_list
print(month_born)

my_other_list.append("Contento")

my_other_list.insert(2, 39)

my_other_list.remove(39)

my_other_list[2] = "40"
print(my_other_list)

print(my_lists.pop())
print(my_lists)

my_pop_element = my_lists.pop(2)
print(my_pop_element)
print(my_lists)

my_new_list = my_lists.copy()
my_lists.clear()
print(my_lists)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

print(my_new_list[1:4])

