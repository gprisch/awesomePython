import re

mobile = '06-09-00-15-45'

pattern1 = r'\d\d-\d\d-\d\d-\d\d-\d\d'

if re.match(pattern1, mobile):
    print(f'{mobile} is accepted')
else:
    print(f'{mobile} is rejected')
