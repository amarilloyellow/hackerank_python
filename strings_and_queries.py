import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    # Write your code here
    returnList = list()
    for query in queries:
        count = 0
        for string in strings:
            if query == string:
                count += 1
        returnList.append(count)

    return returnList            

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc', 'er']
    queries = ['ab', 'abc', 'bc', 'er', 'ty', 'ert']
    print(matchingStrings(strings,queries))