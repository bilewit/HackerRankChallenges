# https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    foo_dict = dict()
    s = list(s)
    s.sort()
        
    #init/fill dict
    for letter in s:
        if letter in foo_dict.keys():
            foo_dict[letter] += 1
        else:
            foo_dict[letter] = 1
        
    #sort dict 
    foo_dict = sorted(foo_dict.items(), key=lambda x: x[1], reverse=True)
    
    #print results
    for x in range(3):
        print(foo_dict[x][0],foo_dict[x][1])
