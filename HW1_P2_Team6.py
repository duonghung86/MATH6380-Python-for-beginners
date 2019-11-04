"""

@authors: Johnny and Thanh

"""

# Program computes the balance of a savings account after
# a certain number of years. 


# p is the principal amount that was originally deposit into the account. 
p = float(input('How much will you deposit into the account? '))

# r is the annual interest rate paid by account.
r = float(input('This account pays an annual interest of (NOTE: Enter \
interest in decimal form): '))

# n is the number of times per year the interest is compounded.
n = int(input('This interest will be compunded how many times?'+
              '(For example, if interest is compounded monthly, enter 12.'+
              'If interest is compounded quarterly, enter 4.) :'))

# t is the number of years principal will be left to earn interest. 
t = int(input('How many years will you leave this money to accrue? : '))

# a is the amount of money in the account after t years.
# Formula for calculating balance after t years
a = p * (1 + (r / n)) ** (n * t)

print('\nAfter ' + str(t) + ' years, the amount of money that will be on the \
account is $' + str(round(a,2)))