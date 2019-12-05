from decimal import Decimal

"""
A person invests $1000 in a savings account yielding 5% interest. Assuming that
the person leaves all_nums interest on deposit in the account, calculate and display the
amount of money in the account at the end of each year for 10 years. Use the following
formula for determining these amounts:
a = p(1 + r)n
where
p is the original amount invested (i.e., the principal),
r is the annual interest rate,
n is the number of years and
a is the amount on deposit at the end of the nth year.
"""

principal = Decimal('1000.00')
interest_rate = Decimal('0.05')
number_of_years = 10
amount = 0

for year in range(1, 11):
    amount = principal * (1 + interest_rate) ** year
    print(f'year {year:>2}: {amount:>10.2f}')
