import random

# print an unpacked list
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(*ls)  # instead of print(ls)

# one line if
counter = 0
for i in range(3):
    print(f'Oh yes I was called '
          f'{counter} time'
          f'{"s" if counter > 1 else ""}')
    counter += 1

# default values
# # set the variable to true to test
test_this = True
password_required = False
if test_this:
    username, password = input('enter your user name: ').strip() \
                         or 'anonymous', \
                         input('enter your password: ').strip() \
                         if password_required else None
    print(username,
          ''.join(['*' for c in list(password)])
          * random.randrange(2, 5)  # lol
          if password is not None else '',
          sep='\n')
