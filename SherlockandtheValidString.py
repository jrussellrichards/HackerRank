import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # Go over string and count how many times string occured
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # count how many times a count occured
    min_count = int(char_dict[min(char_dict, key = lambda charx: char_dict[charx])])
    max_count = int(char_dict[max(char_dict, key = lambda charx: char_dict[charx]) ])
    dif_max_min = max_count - min_count

    number_of_max = 0
    for char in char_dict: 
        if char_dict[char] == max_count: 
            number_of_max = number_of_max + 1
    number_of_MIN = 0
    for char in char_dict: 
        if char_dict[char] == min_count: 
            number_of_MIN = number_of_MIN + 1
    #number_of_max = max(filter(lambda x: x[char]==max_count, char_dict))
    # final test:
    if len(char_dict) == 1:
        return 'YES'
    if s == number_of_max:
        return 'YES'
    if number_of_max>1 and number_of_MIN != 1:
        return 'NO'
    else :
        if number_of_max == 1 and dif_max_min == 1:
            return 'YES'
        if number_of_MIN == 1 and dif_max_min == 1:
            return 'YES'

        else:
            return 'NO'

s = 'aabbc'

print(isValid(s))