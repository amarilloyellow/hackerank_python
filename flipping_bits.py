#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    valorRe = ''
    valorFinal= 0
    div = n
    while div > 1:
        if div%2 == 1:
            valorRe += '0'
        else:
            valorRe += '1'
        div = int(div/2)

    if n == 0:
        valorRe += '1' + ('1'* (31-len(valorRe)))
    else:
        valorRe += '0' + ('1'* (31-len(valorRe)))
    
    valorFinal = 1 * int(valorRe[0])
    acm = 1
    for i in range(len(valorRe)-1):
        acm *= 2
        print(acm)
        valorFinal += acm * int(valorRe[i+1])

    return valorFinal

if __name__ == '__main__':
    print(flippingBits(0))