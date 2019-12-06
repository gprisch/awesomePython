from copy import deepcopy


# 2 keep it dry
def init_list():
    ls = [1, 2, [3, 4]]
    return ls


def update_copy():
    global my_copy
    my_copy[0:2] = [0] * 2
    my_copy[2][0] = my_copy[2][1] = 0


my_list = init_list()
my_copy = my_list[:]
# a shallow copy

assert my_list is not my_copy
assert my_list == my_copy
assert my_list[2] is my_copy[2]  # Ahhhhhh.... same list reference in the 2 lists

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

# enter the matrix
# Can we init a matrix like this?
a_shallow_matrix = [[0] * 3] * 4
print(a_shallow_matrix)
# but in fact we create 4 references, let s check
assert a_shallow_matrix[0] is a_shallow_matrix[1]
# so if we change the reference we get this
a_shallow_matrix[0][0] = 1
print(a_shallow_matrix)
# [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

# instead, we use comprehensions
a_deep_matrix = [[0] * 3 for _ in range(4)]
print(a_deep_matrix)
assert a_deep_matrix[0] is not a_deep_matrix[1]  # ok
a_deep_matrix[0][0] = 1
assert a_deep_matrix[0][0] != a_deep_matrix[0][1]  # ok

# 3, 4 .... dimensions matrix
hypercube = [[[0] * 2 for _ in range(2)] for _ in range(3)]
print('My first cell in cube =', hypercube[0][0][0])

