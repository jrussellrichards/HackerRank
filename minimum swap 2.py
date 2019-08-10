#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumSwaps function below.
# Solucion: Se verifica por cada posicion (desde 0 hasta n-1) si cada elemento ubicado en ella es el que corresponde,
# de no serlo se realiza un swap para ubicarlo donde corresponde. Se verifica nuevamente si el nuevo elemento en 
# esa posicion es el que corresponde, se repite esto hasta que coincida. Una vez realizado esto se repite 
# el procedimiento para cada posicion. 

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

answer=minimumSwaps([7, 1, 3, 2, 4, 5, 6])

print(answer)

