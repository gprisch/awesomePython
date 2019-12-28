import re

from termcolor import cprint, colored, COLORS

mobile = '06 09-00-15-45'

# raw string
pattern1 = r'\d\d-\d\d-\d\d-\d\d-\d\d'
# add end of line $ ans start of line ^
pattern2 = r'\A\d\d-\d\d-\d\d-\d\d-\d\d$'
pattern3 = r'\A[0-9]{2}[ -]\d\d-\d\d-\d\d-\d\d$'
pattern4 = r'\A[0-9]{2}[ -]\d{2}-\d{2}-\d{2}-\d{2}'

for k, v in COLORS.items():
    print(f'{k}', end='  ')
print('\n')

if re.fullmatch(pattern4, mobile):
    cprint(f'{mobile} is accepted', 'green', on_color='on_white', attrs=['bold'])
else:
    print(f'{mobile} is {colored("rejected", "grey", "on_red")}')

a_str = 'this is'


def test_exp(p):
    global a_str
    if re.match(p, a_str):
        print('match')
    else:
        print('no match')


# start of line
pattern = r'\At'
test_exp(pattern)
# word boundaries
pattern = r'\b.+s\si*'
test_exp(pattern)
# test presence of one digit

res = re.match(r'\w*\d', 'aaaaajdld9hhhh')
assert res is not None

res = re.match(r'g(r{4,})(ego)(r.*)', 'grrrrrrrrrrregoryyyyy')
for i in range(res.lastindex + 1):
    print(f'{i}:{res.group(i)}', sep=' ')

