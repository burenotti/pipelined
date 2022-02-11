from pipelined import *
from pipelined.shortcuts.math import *


# Parses input and converts

# data = input().split() | as_(int) | to_list
#
# print(data)

data = [1, -15, 3, 4, 12]


# Get only numbers positive
# Also you need to create a list from the values
# because data | where(is_positive) is exactly filter(is_positive, data)
# and filter executes lazily.

data = data | where(is_positive) | to_list


# get square of each number
# (apply is map, so you still need to create list)

data = data | apply(lambda x: x * x) | to_list

# or use squared from shortcuts

data = data | apply(squared) | to_list
