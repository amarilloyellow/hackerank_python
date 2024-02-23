import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    s = s.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(abc)):
        tieneEsa = False
        for j in range(len(s)):
            if abc[i] == s[j]:
                tieneEsa = True
        if tieneEsa == False:
            return "not pangram"
            break       
    return 'pangram'
            

print(pangrams('We promptly judged antique ivory buckles for the prize'))
