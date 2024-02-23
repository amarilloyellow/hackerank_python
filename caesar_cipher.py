

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    s = list(s)
    llave = [list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' * k),list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' * k)] 
    
    for i in range(len(s)):
        if s[i] in llave[0]:
            s[i] = llave[0][llave[0].index(s[i]) + k]
        elif s[i] in llave[1]:
            s[i] = llave[1][llave[1].index(s[i]) + k]
    return ''.join(s)



print(caesarCipher('middle-Outz',2))