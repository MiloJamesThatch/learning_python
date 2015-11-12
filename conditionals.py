import random
import sys
import os

age = 21

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

age = 30

if ((age >= 1) and (age >= 18)):
    print('You get a birthday')
elif (age == 21) or (age >= 65):
    print('You get a birthday too')
elif not (age == 30):
    print('You do not get a birthday')
else:
    print('No one gets a birthday')

# after a condition is met, nothing else below matters until after ELSE
