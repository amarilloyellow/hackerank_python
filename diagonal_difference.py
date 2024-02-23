import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    diagonales = [0,0]
    for i in range(len(arr)):
        diagonales[1] += arr[i][(len(arr)-1)-i]
        diagonales[0] += arr[i][i]
        diferencia = abs(diagonales[0] - diagonales[1])

    return diferencia



newMatrix = [
    [1,2,3],
    [4,5,6],
    [9,8,9]
    ]

print(diagonalDifference(newMatrix))
