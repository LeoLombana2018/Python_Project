### tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (38, 1.67, "Leonardo", "Lombana")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-2])

print(my_tuple.count(38))
print(my_tuple.index("Leonardo"))

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)
print(type(my_tuple))