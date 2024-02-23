#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    n = len(arr)
    # arr = arr * k
    arr.sort()
    res = max(arr[0:k]) - min(arr[0:k])
    for i in range(n-k):
        # print(arr[i:i+k], '\nMinimo:', min(arr[i:i+k]), 'Maximo:', max(arr[i:i+k]), '\nResultado:', (max(arr[i:i+k]) - min(arr[i:i+k])))
        if (max(arr[i:i+k]) - min(arr[i:i+k])) < res:
            res = max(arr[i:i+k]) - min(arr[i:i+k])   
            # print('-----------------Estes-----------------------')     
    print(res)





f = open ('maxmin2.txt','r')
mensaje = []
for i in range(100002):
    mensaje.append(int(f.readline().strip()))
f.close()

maxMin(mensaje[1], mensaje[2:len(mensaje)])

""" arreglo = mensaje[2:len(mensaje)]
arreglo.sort()
# print(arreglo[-10:len(arreglo)])
arreglo += arreglo[0:10]
print(arreglo) """

# print(maxMin(2, [1,2,1,2,1]))
