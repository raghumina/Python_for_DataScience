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
economical_rate = min(cpm_1,cpm_2,cpm_3)
print(economical_rate)
