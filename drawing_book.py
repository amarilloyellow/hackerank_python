#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    izq_der = int(p/2)
    der_izq = int(((n/2)) - izq_der)

    print(izq_der, der_izq)
    
    # return izq_der if izq_der<der_izq else der_izq



pageCount(5,4)