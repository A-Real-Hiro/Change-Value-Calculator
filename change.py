# Change calculator
# Author: Edgar Becerril 
# Date Created: 5/8/2021
# Last Modified: 12/28/2021
# q = float variable for quarters
# d = float variable for dimes
# n = float variable for nickels
# p = float variable for pennies
# user is asked for input for how many of each coin is present and then the amount that the change adds up to is calculated
# and shown to the user.

q = float(input("Please enter number of quarters: ")) * 0.25
d = float(input("Please enter number of dimes: ")) * 0.10
n = float(input("Please enter number of nickels: ")) * 0.05
p = float(input("Please enter number of pennies: ")) * 0.01

# totals the change
T = q + d + n + p

# displays the change to the user
print("Total amount of change: $", '{0:.2f}'.format(T))