#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    
    visited_elements = { i : False for i in arr }
    copy_arr=copy.copy(arr)
    cycles=[]
    cycle=[]
    element=arr[0]
    visited_elements_count=0
    answer=0
    while(len(copy_arr)!=0):
        if(visited_elements[element]==False):
            visited_elements[element]=True
            cycle.append(element)
            visited_elements_count+=1
            element=arr[element-1]
            copy_arr.remove(element)
        else:
            cycles.append(cycle)
            cycle=[]
            element=copy_arr[0]
        if(len(copy_arr)==0):
            cycles.append(cycle)
    
    for cycle in cycles:
        answer+=len(cycle)-1

    return answer

answer=minimumSwaps([4 ,3 ,1 ,2])

print(answer)

