import os

file = open('at-python.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line[::-1])