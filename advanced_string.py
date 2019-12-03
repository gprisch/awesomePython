# numeric conversions
binary = int('11000000', 2)
assert binary == 192
hexadecimal = int('ff', 16)
assert hexadecimal == 255
octal = int('117', 8)
assert octal == 79
assert f'{1:08b}' == '00000001'
assert 'hello'.__contains__('hell') is True
assert ('Hell' in 'Hello') is True
assert ('hElLo'.casefold() == 'helLo'.casefold()) is True

# String reversed_str
a_string = 'Hello, my name is Greg'

reversed_str = a_string[::-1]
assert reversed_str == 'gerG si eman ym ,olleH'
# reverse part of String
a_part_rev = a_string[::2]
print(a_part_rev)
b_part_rev = a_string[13:5:-1]
assert b_part_rev == 'eman ym '

assert ord('A') == 65
assert chr(65) == 'A'

