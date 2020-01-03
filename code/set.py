# create a set
my_set = set()
# make it immutable
frozenset(my_set)

# another with unique values
another_set = set(list(range(8)) + list(range(9)))

# CRUD
another_set.add(10)
assert 10 in another_set
another_set.update({11})

assert 11 in another_set
another_set.clear()
assert len(another_set) == 0
assert not another_set
another_set.update('hello')
another_set.remove('h')

set1 = list(range(10))
set2 = list(range(12))
set2.remove(3)

# compare
assert set1 != set2
# read < is a subset
assert set1 < set2
# equal
assert {1, 3, 5} == {1, 3, 5}
# read <= improper subset of
assert {1, 3, 5} <= {1, 5, 3}  # also ==
assert {1, 3} <= {1, 5, 3}
# same but right to left. > must be read  superset of
assert {1, 3, 5, 7} > {3, 5, 1}
# here improper superset
assert {1, 3, 5} >= {1, 5, 3}
assert {1, 3, 5} >= {5, 3}
# but of course we have methods
assert not ({1, 2} <= {1, 5, 3}) or not ({1, 2}.issubset({1, 3, 5}))
assert {1, 3, 5}.issuperset({3, 5, 1})

# operators
an_union = {1, 3, 5} | {2, 3, 4}
another_union = {1, 3, 5}.union([2, 3, 4])
assert an_union == another_union

an_intersection = {1, 3, 5} & {2, 3, 4}
another_intersection = {1, 3, 5}.intersection({2, 3, 4})
assert an_intersection == another_intersection

a_difference = {1, 3, 5} - {2, 3, 4}
another_difference = {1, 3, 5}.difference({2, 3, 4})
assert a_difference == another_difference

a_symmetric_diff = {1, 3, 5} ^ {2, 3, 4}
another_symmetric_diff = {1, 3, 5}.symmetric_difference({2, 3, 4})
assert a_symmetric_diff == another_symmetric_diff

assert {1, 3, 5}.isdisjoint({2, 4})

#  we can use these ops as well. example:
sym_diff_update = {1, 3, 5}
sym_diff_update ^= {2, 3, 4}
# same than (was {1, 2, 4, 5})
sym_diff_update.symmetric_difference_update([5, 7])
# now {1, 2, 4, 7}
# available: |= (update()), &= (intersection_update())
# -= (difference_update())

# comprehensions
evens = {item for item in range(10, 100) if item % 2 == 0}
odds = set(range(10, 100)) - evens
assert evens.isdisjoint(odds)
all_nums = odds | evens
assert all_nums == set(range(10, 100))



