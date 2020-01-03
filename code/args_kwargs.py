ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

counter = 0


# splat or positional expansion operators
# * defines a list
# ** defines a dictionary
def many_args_func(a: int, *lst, **kwargs):
    p = kwargs.get('print_counter')
    global counter
    counter += 1

    if p:  # just to show kwargs. This code is bad
        print(f'Oh yes I was called '
              f'{counter} time'
              f'{"s" if counter > 1 else ""}')
    return a, len(lst)


# alias the function
fn = many_args_func  # useful for API, no?
print(f'{fn.__name__} called')
assert fn(2, ls, print_counter=True) == (2, 1)
# ls is a list in a tuple ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],)
assert many_args_func(2, 3, 4, 5, 6, print_counter=True) == (2, 4)
# args: (3, 4, 5, 6)
assert counter == 2
