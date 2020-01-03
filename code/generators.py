# create an iterator

# iterator = reversed([1, 2, 3, 4])
# for i in iterator:
#     print(i, end=' ')


def make_evens_gen():
    for j in range(2, 11, 2):
        yield j


generator = make_evens_gen()  # return a generator
next(generator)


def make_fibo_gen(n):
    a, b = 1, 1
    while a <= n:
        print(a)
        yield a
        a, b = a + b, a


gen = make_fibo_gen(50)

# first call
# 1 in gen
# 1
# Out[42]: True

# second call (previous state is kept)
# 3 in gen
# 2
# 3
# Out[43]: True

a_gen = (i for i in range(1, 5))

for stuff in a_gen:
    print(stuff, end='  ')


# yield from
def my_sub_gen(x):
    for i in range(x):
        yield i


def my_gen(x):
    yield from my_sub_gen(x)


for j in my_gen(8):
    print(j, end='  ')

