import re

from termcolor import cprint, colored, COLORS

mobile = '06 09-00-15-45'

# raw string
pattern1 = r'\d\d-\d\d-\d\d-\d\d-\d\d'
# add end of line $ ans start of line ^
pattern2 = r'^\d\d-\d\d-\d\d-\d\d-\d\d$'
pattern3 = r'^[0-9]{2}[ -]\d\d-\d\d-\d\d-\d\d$'

for k, v in COLORS.items():
    print(f'{k}', end='  ')
print('\n')

if re.fullmatch(pattern3, mobile):
    cprint(f'{mobile} is accepted', 'green', on_color='on_white', attrs=['bold'])
else:
    print(f'{mobile} is {colored("rejected", "grey", "on_red")}')
