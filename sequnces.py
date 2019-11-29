# list
my_list = [-45, 6, 0, 72, 17]
# negative indexes are ok
assert my_list[4] == my_list[-1]
# mutable
my_list[-2] = 18
assert my_list[3] == 18
# permute elements
my_list[0], my_list[1] = my_list[1], my_list[0]
assert my_list[0] == 6 and my_list[1] == -45
# concat lists
list1 = [10, 20, 30]
list2 = [40, 50]
assert list1 + list2 == [10, 20, 30, 40, 50]
# compare 2 lists
list3 = [10, 20, 31]
assert list3 > list1
assert list2 > list3

# tuples
empty_tuple = ()
assert len(empty_tuple) == 0
# packed tuple
student_tuple = 'John', 'Green', 3.3
assert len(student_tuple) == 3
# parenthesis are recommended
another_student_tuple = ('Mary', 'Red', 3.3)
# unpack into distinct variables
first_name, last_name, grade = another_student_tuple
# print(first_name, last_name, grade, sep=' ')
assert another_student_tuple[0] == 'Mary'
# one element
a_singleton_tuple = ('red',)  # note the comma
# append tuple to list
numbers = [1, 2, 3, 4, 5]
numbers += (6, 7)
assert [1, 2, 3, 4, 5, 6, 7] == numbers
a_tuple = (1, 2)
assert a_tuple < (6,)
# tuples are immutable
# a_tuple[0] = 3
# but contain mutable objects
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[2][0] = 90
assert student_tuple == ('Amanda', 'Blue', [90, 75, 87])

# unpack other sequences
x, y = 'hi'
assert x == 'h' and y == 'i'
x, y = [1, 3]
assert x == 1 and y == 3
x, y = {2, 4}
assert x == 2 and y == 4
x, y = [{1, 2}, [1, 3]]
assert x == {1, 2} and y == [1, 3]

