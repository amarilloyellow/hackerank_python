#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.n
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pares = 0
    elm = list(set(ar))
    for i in range(len(elm)):
        pares += int(ar.count(elm[i])/2)
    return pares

sockMerchant(7,[1,2,1,2,1,3,2])