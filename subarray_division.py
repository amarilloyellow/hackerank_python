
import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # ways = [sum(s[i:i+m]) for i in range(len(s)-m+1)]
    for i in range(len(s)-m-1):
        ways = sum(s[i:i+m])
    return ways


print(birthday([2,2,1,3,2],4,2))