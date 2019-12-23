import math
import statistics

dices_result = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
# variance
# 1. the "manual process" is:
# mean (this is the VERY explicit way to do it)
dices_result_sum = 0
dices_result_length = 0
for i in dices_result:
    dices_result_sum += i
    dices_result_length += 1

assert dices_result_sum == 35
assert dices_result_length == 10
dices_result_mean = dices_result_sum / dices_result_length
assert dices_result_mean == 3.5  # 35 / 10 = 3.5
# for each element of the list we subtract the mean
dices_result_minus_mean = []
for i in dices_result:
    dices_result_minus_mean.append(i - dices_result_mean)

assert dices_result_minus_mean == [-2.5, -0.5, 0.5, -1.5, 2.5, 1.5, -0.5, 0.5, 1.5, -1.5]

# then we calculate the square of every element
squares = []
for i in dices_result_minus_mean:
    squares.append(i ** 2)
assert squares == [6.25, 0.25, 0.25, 2.25, 6.25, 2.25, 0.25, 0.25, 2.25, 2.25]
# finally the squares mean (we use a quicker way) to get the population variance
population_variance_explicit = sum(squares) / len(squares)

# 2. with the statistics module
population_variance = statistics.pvariance(dices_result)

assert population_variance == population_variance_explicit == 2.25

# standard deviation
# square of the variance
assert math.sqrt(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])) \
       == statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]) == 1.5

# just for observation
print(statistics.pvariance([1, 2, 1, 1, 1, 1, 300000]))
print(statistics.pvariance([12, 2, 1, 1, 1, 1, 3]))
print(statistics.pvariance([112, 112, 112, 112, 112, 112, 112]))
print(statistics.pvariance([112.1, 112, 112, 112, 112, 112, 112]))