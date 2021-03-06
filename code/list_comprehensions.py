# List Comprehensions (greedy evaluation)
one_line_list = [i ** 2 for i in range(1, 11) if i % 2 == 0]
assert one_line_list == [4, 16, 36, 64, 100]
# update it
one_line_list = [item - 2 for item in one_line_list]
assert one_line_list == [2, 14, 34, 62, 98]

# Generator Expressions (lazy evaluation)
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for index, value in enumerate((x ** 2 for x in numbers if x % 2 == 0)):
    print(index, value, sep=':', end='\n')

# ready to generate on demand
squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
assert tuple(squares_of_odds) == (9, 49, 1, 81, 25)

# filtering with Lambda
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
filtered = list(filter(lambda x: x % 2 != 0, numbers))
assert filtered == [3, 7, 1, 9, 5]
# map
mapped = list(map(lambda n: n % 2, numbers))
same = [item % 2 for item in numbers]
assert mapped == same == [0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
# print(vowel for vowel in 'aeiou')
colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
assert ('Red' < 'orange') is True
# because
assert ord('R') == 82
assert ord('o') == 111
min_color = min(colors, key=lambda color: color.lower())
assert min_color == 'Blue'
# alphabetic order of colors
assert sorted(colors, key=lambda c: c.lower()) == ['Blue', 'green', 'orange', 'Red', 'Yellow']

vowels = 'aeiou'


