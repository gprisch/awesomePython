import random

print(__name__)


# a simple function
def perimeter_rectangle(length, width=2):
    """ Calculates the perimeter of a rectangle """
    return length * width


print(perimeter_rectangle(width=17, length=12))


# just a test on random functions
def roll_dice(times, seed_id):
    if seed_id:
        random.seed(seed_id)
    rolls = []
    for roll in range(times):
        rolls.append(random.randrange(1, 7))
    return rolls


# same seed_id, same list
assert roll_dice(10, 32) == roll_dice(times=10, seed_id=32)
# else different
assert roll_dice(10, None) != roll_dice(10, None)


# variant number of arguments
def average(*args):
    return sum(args) / len(args)


an_average = average(1, 2, 3, 4, 4)
print(an_average)

# it works with iterables (star before the iterable name)
a_set = {1, 3, 7, 8, 9}
set_average: float = average(*a_set)
print(set_average)

x = 5


def modify_global():
    global x # global affects the x at the global scope
    x = 'Hello'
    print('global_scope() x =', x)

modify_global()
print(x)
