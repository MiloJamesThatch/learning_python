import random
import sys
import os

# cannot join maps(dictionaries) together like lists or tuples

known_names = {'Dead Space': 'Issac Clark',
               'The Evil Within': 'Seb Con',
               'Minecraft': 'Steve'}
print(known_names['Minecraft'])

del known_names['Dead Space']

print(known_names.get('The Evil Within'))
print(known_names.keys())
print(known_names.values())
