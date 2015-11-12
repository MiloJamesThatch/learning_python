import random
import sys
import os

print("Hello World")

# Variables

name = "Milo"
print(name)
age = 18
print(age)

# Math

print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2) # remainder
print("5 ** 2 =", 5 ** 2) # exponents
print("5 // 2 =", 5 // 2) # divide and drop the decimal down

# Strings

quote = '"This is a quote inside of quotes'""

multi_line_quote = '''this is a
multi line quote'''

new_string = quote + multi_line_quote

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
