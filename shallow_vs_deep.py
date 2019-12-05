from copy import deepcopy


# 2 keep it dry
def init_list():
    ls = list(range(1, 3))
    ls.append([3, 4])
    return ls


def update_copy():
    global my_copy
    my_copy[0:2] = [0, 0]
    my_copy[2][0] = my_copy[2][1] = 0


my_list = init_list()
my_copy = my_list[:]
# a shallow copy

assert my_list is not my_copy
assert my_list == my_copy
assert my_list[2] is my_copy[2]  # Ahhhhhh.... same list in the 2 lists

update_copy()

print(my_list, my_copy)
# [1, 2, [0, 0]] [0, 0, [0, 0]]
# list in the list is a reference !!

# now let us deep copy
my_list = init_list()
my_copy = deepcopy(my_list)
assert my_list[2] is not my_copy[2]  # different nested lists thx 2 deep copy

update_copy()

print(my_list, my_copy)
# [1, 2, [3, 4]] [0, 0, [0, 0]]
