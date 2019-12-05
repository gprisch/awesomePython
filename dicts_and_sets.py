days_per_month = {'January': 31, 'February': 28, 'March': 31}
# iterate through
for month, day in days_per_month.items():
    print(f'Month {month} has {day}')
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

# CRUD
roman_numerals['L'] = 50
roman_numerals['II']
roman_numerals['X'] = 10
del roman_numerals['III']  # ot
roman_numerals.pop('X')
print(roman_numerals)
# safe read
roman_numerals.get('III')
# test if key is present
'III' not in roman_numerals

# keys and values
months = {'January': 1, 'February': 2, 'March': 3}
months['December'] = 12
print(months.keys())

# convert keys in list
print(list(months.keys()))
# a list of tuples
print(list(list(months.items())))

# sorted keys
for month in sorted(months.keys()):
    print(month, end=' ')

# comparisons
country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussels'}

assert country_capitals1 is not country_capitals2
assert country_capitals2 != country_capitals1


