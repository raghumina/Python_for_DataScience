# In this file i am solving  the python problems
# i am practicing a lot of python problems
# problems may be or may not be related to data Science

'''
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
principal = 150000

# Rate of interest
rate = 12

# Time period
time = 2

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


# The Fibonacci series is the sequence of numbers where each number is the sum of two preceding numbers. For example – 1, 1, 2, 3, 5, 8, 13, 21 and so on.
#
# Let’s look at a function to return Fibonacci series numbers using loops.
#

def fibonacci(n):
    """ Returns Fibonacci Number at nth position using loop"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    i1 = 0
    i2 = 1

    num = 1
    for x in range(1, n):
        num = i1 + i2
        i1 = i2
        i2 = num
    return num


for i in range(10):
    print(fibonacci(i), end=" ")

#

# Assign value of 12 to a new variable 'age' and "John" to 'name'.
# Save the type of age using type(age) and save it to a variable type_age
# Similarly save the type of name to a variable type_name
# Print out the variables type_age and type_name using the print() function

age = 12
name = "John"
type_age = type(age)
type_name = type(name)
print(type_age)
print(type_name)

#
# Calculate the Compound Interest
# In this problem, you will calculate the compound interest (C.I.).
# Remember that the formula for compound interest for the amount after n years is
# A = P(1 + r/100)^n
# A=P(1+r/100)
# n
#
# Here, A is the Amount after n years, r is the rate of interest, and P is the principal.
#
# Your task is to calculate the amount after two years on a principal amount of USD 1000 at the rate of 10 % p.a.
#
# Instructions
# Store principal, rate of interest and time in variables P, r, and n respectively.
#
# Now calculate the amount according to the formula given above and save it in a variable A.
#
# Calculate A - P and store the result in a variable called interest.
#
# Print out interest using the print() function.

# Code starts here

# store variable names
n = 2
P = 1000
r = 10

# compound interest formula
A =  P*(1 + (r / 100))**n

# display compound interest
print(A)

# display interest
interest = A - P
print(interest)

# Code ends here
'''

# PROBLEM
#
# You are given two strings, "Monty" and "Python".
# Follow the instructions below to carry out string operations like concatenation, indexing, slicing, etc.:
#
# Two variables name and title with values "Monty" and "Python", are given.
#
# Conatenate (+) name and title and save it to variable called full_name. (Note:
# Add a whitespace between name and title while concatenating)
#
# Use slicing to pick up the first name from full_name and save it to a first_name variable.
#
# Calculate the length of the full name using the len() function. Subtract 1 from it
# (so that you get rid of the whitespace) and save it to a len_name variable.
#
# Check whether the alphabet "f" is in the full name and save it to a is_f variable.
#
# Now, split the full name back into first name and title using the .split() method on the full_name variable.
# Save it to a split variable. The output will come as a list which is another important data structure.
# You will learn more about it in the next chapter.
#
# Print the full_name, first_name, len_name, is_f and split variable to check your results.
#
# Test Cases: The value of full_name should be "Monty Python".
# The value of first_name should be "Monty".
# The value of len_name should be 11.
# The value of is_f should be False.
# First element of split should be "Monty".
# Second element of split should be "Python".

#
name  = "Monty"
title = "Python"
full_name = name + title
print(full_name)
first_name = full_name[0:5]
print(first_name)

