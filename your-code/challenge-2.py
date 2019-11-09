"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
#Importing all libraries at once
import random
import string
import sys

#Simplified the list of characters by using string methods.
char = [string.ascii_lowercase + string.digits]
wordlist = [ch for ch in char]

def Rand_Str_Gen(l=12, a=wordlist):
    p = 0
    string = ''
    while p<l:
        string += random.choice(a)
        p += 1
    return string

def Batch_Str_Gen(n, min_len=8, max_len=12):
    str_list = []
    for r in range(n):
        result = None
        if min_len < max_len:
            result = random.choice(range(min_len, max_len))
        elif min_len == max_len:
            result = min3_len
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        str_list.append(Rand_Str_Gen(result))
    return str_list

min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
num_str = input('How many random strings to generate? ')

print(Batch_Str_Gen(int(num_str), int(min_len), int(max_len)))
