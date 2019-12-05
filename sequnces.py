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
# enumerate function
words = ['Amanda', 'Blue', 'hello', 'world']
for index, word in enumerate(words):
    print(f'{index}: {word:>7}')
# 2 examples
colors = ['red', 'orange', 'yellow']
assert list(enumerate(colors)) == [(0, 'red'), (1, 'orange'), (2, 'yellow')]
assert tuple(enumerate(colors)) == ((0, 'red'), (1, 'orange'), (2, 'yellow'))
assert set(enumerate(colors)) == {(0, 'red'), (1, 'orange'), (2, 'yellow')}
# bar chart example
numbers = [19, 3, 15, 7, 11]
print('\nCreating a bar chart from numbers:')
print(f'index{"value":>8}   bar')
for i, v in enumerate(numbers):
    print(f'{i:>5}{v:>8}   {"|" * int(v)}')
# slicing sequences
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
assert numbers[2:4] == [5, 7]
assert numbers[6:] == [17, 19]
assert numbers[:6] == [2, 3, 5, 7, 11, 13]
# with steps
assert numbers[::2] == [2, 5, 11, 17]
# assert numbers[::-1] == numbers.reverse()
# print(numbers.reverse())
# negative indices
assert numbers[-3:-5:-1] == [13, 11]
# delete the numbers
del numbers[2:]
assert numbers == [2, 3]
del numbers
# -> deleted from session
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
assert numbers.index(7) == 1
# are all_nums or any in the list is true
assert all([0, 12]) is False
assert all([3, 12]) is not False
# joke
it = 1
assert it is not False
# more
l = []
l.extend('abc')
assert l == ['a', 'b', 'c']
assert l.count('a') == 1
# copy
cp = l.copy()
assert id(cp) != id(l)

# A, B, C list
for i, el in enumerate(['one', 'two', 'three'], start=65):
    a_b_c_list = f'{chr(i)}. {el}' # A. one ---- B. two etc
    # print(a_b_c_list)

l[0:0] = [1, 2]
assert l == [1, 2, 'a', 'b', 'c']

# useful
assert l * 2 == [1, 2, 'a', 'b', 'c', 1, 2, 'a', 'b', 'c']
assert (None in l) is False
l.append([])
assert ([] in l) is True