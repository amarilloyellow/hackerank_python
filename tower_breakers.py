#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    return 2 if ((n*m)-(n*m-n))%2 == 0 else 1
    

print(towerBreakers(2,2)) # > 2
print(towerBreakers(1,4)) # > 1

print(towerBreakers(1,7)) # > 1
print(towerBreakers(3,7)) # > 1
print(' ')
print(towerBreakers(100000,1)) # > 2
print(towerBreakers(100001,1)) # > 2
print(towerBreakers(374635,796723)) # > 1
print(towerBreakers(950929,183477)) # > 1
print(towerBreakers(732159,779867)) # > 2
print(towerBreakers(598794,596985)) # > 2
print(towerBreakers(156054,445934)) # > 1
print(towerBreakers(156030,99998)) # > 1
