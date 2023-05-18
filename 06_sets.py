### sets ###

my_set = set()
my_other_set = {}

my_other_set = {"Leonardo", "Lombana", 38}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("red")
print(my_other_set)

print("red" in my_other_set)

my_other_set.remove("red")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
print(my_other_set)

