# In this file i am solving  the python problems
# i am practicing a lot of python problems
# problems may be or may not be related to data Science


# Problem 1
# Best cellular plan
# Find the most economical cellular plan in terms of cheapest per minute calling cost
#
# Instructions
# We have provided you with details of 3 plans available to you.
#
# Divide no. of minutes by the price for each plan and save the result in cpm_1, cpm_2 and cpm_3 respectively
# (Meaning divide price_1 by nom_1 and store the result in cpm_1, so on and so forth)
#
# Print cpm_1, cpm_2 and cpm_3
#
# Write the following line of code to find the minimum amongst the variables calculated above
#
# economical_rate= min(cpm_1,cpm_2,cpm_3)

# Details of Plan 1
nom_1 = 100
price_1 = 35

# Calculate the value of plan 1
cpm_1 = price_1 / nom_1
print(cpm_1)
# Details of Plan 2
nom_2 = 125
price_2 = 39

# Calculate the value of plan 2
cpm_2 = price_2 / nom_2
print(cpm_2)

# Details of Plan 3
nom_3 = 180
price_3 = 45

# Calculate the value of plan 3
cpm_3 = price_3 / nom_3
print(cpm_3)

# Find minumim of three
economical_rate = min(cpm_1, cpm_2, cpm_3)
print(economical_rate)


# Problem 2
# Using python programming, help calculate the interest amount your friend needs to give.
#
# Instructions
# The principal amount, rate of interest and time period are stored in the variables principal,
# rate and time respectively
# Apply the formula of simple interest and store the result in a variable called 'simple_int'

# Principal amount
principal=150000

# Rate of interest
rate= 12

# Time period
time=2

# Calculate simple interest
simple_int = (principal * rate * time) / 100


# Print simple interest amount
print(simple_int)



# 1. Factorial of an Integer
# The factorial of an integer is calculated by multiplying the integers from 1 to that number.
# For example, the factorial of 10 will be 1*2*3….*10.


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(f'Factorial of 10 = {factorial(10)}')
print(f'Factorial of 5 = {factorial(5)}')

