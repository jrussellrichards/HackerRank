#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    swaps=0
    lenProblem=len(arr)-1
    for position in range(0, lenProblem):
        curren_element=arr[position]
        while (curren_element != position + 1):
            element_in_position_of_current_element = arr[curren_element - 1]
            arr[curren_element - 1] = curren_element 
            curren_element = element_in_position_of_current_element
            swaps += 1

    return swaps

answer=minimumSwaps([4 ,3 ,2 ,1])

print(answer)

