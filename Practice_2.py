
# initial list
scores = [80,90,95,100]


# memory location of initial list
print('Memory loaction initially is ' , id(scores))
print('='*20)
# change value
scores[2] = 99
# display modified list
print(scores)
print('='*20)
# check memory loaction of modified list
print('Memory location of modified list is ' , id(scores))



# Problems related to list etc
# more typical or data related problems

# In this task, you will store the weights of a family of a four weighing of 70, 80, 45 and 50 kg respectively
# in a list and perform do some operations on it to calculate the mean of the weights.
#
# Instructions
# Store the values in a list called weights.
#
# Save the maximum weight from the list using the max() method to a maximum variable. Print it out.
#

# Suddenly, you realize that you have wrongly entered 45 and that should be 48. So,
# it's time to replace the wrong weight with the correct one. Since 45 is in the second index,
# use weights[2] = 48 to replace the value. Display the weights using print()
#
# Now calculate the sum of the weights using the sum() function and save it to a total variable. Print it out.
#
# Calculate the mean of their weights using the formula sum / number of elements and save it to a variable mean.
# Print this out too.

# lets start

weights = [70,80, 45, 50]
print(max(weights))

weights[2] = 48
print(weights)

# we can do it we can do it
# we can go for it
# we can