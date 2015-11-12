import random
import sys
import os

grocery_list = ['Butter', 'Tomatoes', 'Oil', 'Pizza']

print("First item is", grocery_list[0])
# always remember that python starts with 0 like 0 1 2 3

grocery_list[0] = 'More Butter'
print("First item is now", grocery_list[0])
# order of execution is critical

print(grocery_list[1:3])
# prints grocery_list 1 up to 3, but not 3

other_things = ["Wash car", "Pick up check", "Kiss wife"]
to_do_list = [other_things, grocery_list]
print(to_do_list)

grocery_list.append('Food things')
print(grocery_list[4]) # append changes the list for a specific item
grocery_list.insert(1, "Pickles")
print(grocery_list) # insert adds to the list in a specific slot
grocery_list.remove("Pickles") # duh, removes

grocery_list.sort()
grocery_list.reverse()
del grocery_list[3] # deletes slot 3

print(to_do_list)

print(len(to_do_list))
print(max(to_do_list))
print(min(to_do_list))
