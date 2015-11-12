import random
import sys
import os

for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

grocery_list = ['Butter', 'Tomatoes', 'Oil', 'Pizza']

for y in grocery_list:
    print(y)
# a way to cycle through a list

for b in [2, 4, 6, 8, 10]:
    print(b)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for num in range(0, 3):
    for num2 in range(0, 3):
        print(num_list[num][num2])
