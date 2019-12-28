    # string.format()
a_str = "|{1!r:10} loves {0!r:10}|"
formatted_1 = a_str.format('Greg', 'Jean')
print(formatted_1)

another_str = "|{1!s:10} loves {0!s:10}|"
formatted_2 = another_str.format('Greg', 'Jean')
print(formatted_2)

str3 = '{:-^25}'  # center
str4 = '{:->25}'  # right
str5 = '{:-<25}'  # left
print(str3.format('Hello world'))
print(str4.format('Hello world'))
print(str5.format('Hello world'))

# for numeric values
print('{:=10}'.format(-12))
print('{:0=10}'.format(-1245))

# all examples can be executed like this
print(format('Lady','@<10'))

# blank, ) or -, just minuses
print('results >{: 10},{:+10},{:-10}'.format(25, 25, 25))

# large numbers, trailing 0
large1, large2 = 18293044944764648, -10_000_980
print('{:,}'.format(large1))
print('{:-018,}'.format(large2))

# not trailing 0 in the
# next but a group of 0
print('{:0>10}'.format(-16))

# special cases
length = 10
precision = 4
a_format = '{0:{1},.{2}f}'
print(a_format.format(1670.45678, length, precision))  # 1,670.457



