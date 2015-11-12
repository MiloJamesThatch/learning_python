import random
import sys
import os

# tuples cannot be changed after being executed
pi_tuple = (3,1,4,1,5,9)
# however they can be converted into lists
new_list = list(pi_tuple)
# then they can be converted back
new_tuple = tuple(new_tuple)

# can get min, max, len, etc.

len(pi_tuple)
max(pi_tuple)
min(pi_tuple)
