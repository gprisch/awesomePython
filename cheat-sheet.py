import statistics

from decimal import Decimal
# variables
a, b = 10, 5
print(a, ' ', b)
# easy permutation
a, b = b, a
print(a, ' ', b)
a = b = 7
# sep and end
print(a, b, sep=' ')
print(10, 20, 30, sep="-")
for c in 'Hello':
    print(c, end='  ')
print('\n')
# conditional
grade = 100
if grade > 90:
    print('A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
else:
    print('D')
# on one line
result = 'passed' if 51 <= grade <= 100 else 'failed'
print(result)

# range
total = 0
for i in range(10):
    if i == 2:
        continue
    total += i

print(f'total = {total:6}')
print(f'average = {total / 9:.2f}')
print('Hello '[0] * 3)

# iterable
a_list = [2, -3, 0, 17, 9]
a_dictionary = {'first': 1, 'second': 2, 'third': 3}
a_set = {2, 4, 4, 8, 9, 6}

# decimal
a_decimal = Decimal('1000.00')

# statistical functions
a_mean = statistics.mean(a_set)
a_median = statistics.median(a_set)
print(a_mean)
print(a_median)
sorted(a_set)
print(a_set)
print(len(a_set))

another_list = [45, 20, 30, 12]
# mean returns average of the 2 middle values else the middle number (sorted)
print(statistics.median(another_list))
odd_list = [99, 45, 103]
print(statistics.median(odd_list))

# mode is the most frequent number
mode_list = [11, 34, 45, 11, 4, 89]
print(statistics.mode(mode_list))



