import random
import sys
import os


def addNumbers(fNum, lNum):  # creates a function sums up two numbers when placed like (#, #)
    sumNum = fNum + lNum
    return sumNum  # must return to caller


# sumNum does not exist outside of this function

print(addNumbers(1, 4))

# User Input!

print('What is your name?')

name = sys.stdin.readline()  # gathers name from USER in prompt

print('Hello, ', name)  # outputs name in a sentence

long_strng = "I'll catch you if you fall - The Floor"
print(long_strng[0:4])  # outputs first 5 characters
print(long_strng[-5:])  # outputs last 5 characters
print(long_strng[:-5])  # outputs up to last 5 characters
print(long_strng[:4] + "be there")
print("%c is my %s letter and my number %d is %.5f" %
      ("X", "favorite", 1, .14))

print(long_strng.capitalize())
print(long_strng.find("FLoor"))
print(long_strng.isalpha())
print(long_strng.isalnum())
print(len(long_strng))
print(long_strng.replace("Floor", "Ground"))
print(long_strng.strip())  # strips all white space; currently none

quote_list = long_strng.split(" ")  # converts a string into a list
print(quote_list)
