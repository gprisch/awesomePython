from enum import Enum

# multiple line statements
# this:
long_str = 'this string of characters is really long and i need to split it because it is way better'
# the \
long_str = 'this string of characters is\
 really long and i need to split it because\
 it is way better'

# or better with ()
long_str = ('this string of characters is'
            ' really long and i need to split'
            ' it because it is way better')

# good for loops with enumerate
my_list = ['a', 'b', 'c', 'A']
for idx, value in enumerate(my_list, 1):
    print(f'{idx}:{ord(value):>4}')

# Combined assignment operators
# in-place changes to data if
# the object is mutable (such as a list); otherwise, a whole new object is assigned
# to the variable on the left.

str1 = str2 = 'Hello'
print(id(str1), id(str2), sep=' ')
# 140023859862512 140023859862512 identical IDs
assert str1 is str2
str1 += ', World'
print(id(str1), id(str2), sep=' ')
# 140023859909616 140023859862512 are different addresses
assert str1 is not str2
assert str1 == 'Hello, World'

# but lists are mutable and allow
# in places changes that are more
# performing:
str_as_list = list('hello')
str_as_list.extend(list(', world!'))
print(str_as_list)
joined_str = ''.join(str_as_list)
print(joined_str)

# Multiple Assignment and tuple assignments
a = b = c = 0
assert a is b is c
a = 3
assert a is not b and b is c  # so a is not c

a, b = 1, 3
d, e = a + b, a // b
assert a == 1 and b == 3
# cool to test
assert d, e == (4, 0)
a_tuple = (1, 3, 5)
a, b, c = a_tuple
print(a, b, c)
# worst assignment ever seen
locals()['j'] = 12
eval("print(locals()['j'])")
# next is cool
a, *b = 1, 2, 3, 4
assert a == 1 and b == [2, 3, 4]
a, *b, c = range(10)
assert type(a) is int \
       and len(b) == 8 \
       and c == 9
*a, b, c = range(10)  # is possible as well
# List and String “Multiplication”
my_list = [0] * 10000
assert len(my_list) == 10000 \
       and not all(my_list)  # all elements are false (0 in this case)
header = 'A Title'
a_sep = '-' * len(header)
print(header,
      a_sep,
      sep='\n')
assert header.title() and len(a_sep) == 7
# and this is cool as well
a, b, *ls = [i for i in range(10) if i % 2 == 0] * 3
print(a, b, ls)


# 0 2 [4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8]

# Return Multiple Values
def multiple_val(a, b, c):
    return a * 2, b, c


returned = multiple_val(1, 2, 3)
assert type(returned) is tuple
d, e, f = returned
assert d == e == 2 and f == 3


# conditional loops
def find_divisor(n, maximum):
    for i in range(2, maximum + 1):
        if n % i == 0:
            print(i, 'divides evenly into', n)
            break
    else:
        print('No divisor found')


def prompt():
    # not is cool
    while input() == 'y':
        print('continue')
    else:
        print('stop')


# todo uncomment to test it
# prompt()

find_divisor(49, 6)
find_divisor(49, 7)

# not is cool
s = ''
if not s:
    print('Empty String means False')
assert not s

# Treat String as they deserve to be. Chars
palindrome = 'A man, a plan, a canal, Panama!'
palindrome_chars = [c.upper() for c in palindrome if c.isalpha() is True]
assert palindrome_chars == palindrome_chars[::-1]

# chain comparisons are cool
a, b, c = 5, 10, 15
if 0 < a <= c > b > 1:
    print('All these comparisons are true!')
    print('c is equal or greater than all the rest!')


# simulate the switch (no if elif elif else)
class Action(Enum):
    HELLO = 'hello'
    BYE = 'bye'


menu = {
    Action.HELLO: lambda x: print(f'Hello {x}'),
    Action.BYE: lambda x: print(f'Goodbye {x}')
}

# one line for short statements and simulate if else
user_name = input().strip() or 'X'
for k in menu.keys(): menu[k](user_name)

# and use _ for large numbers
my_salary = False and 400_000_000_000
assert my_salary is False  # unfortunately

