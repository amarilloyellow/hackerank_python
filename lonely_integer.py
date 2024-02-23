#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for elmt in a:
        if a.count(elmt) == 1:
            return elmt
    

if __name__ == '__main__':
    a = [1,2,3,4,3,2,1]
    print(lonelyinteger(a))
    