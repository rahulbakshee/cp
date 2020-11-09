'''
https://www.hackerrank.com/challenges/camelcase/problem
Author: rbakshee
'''

#!/bin/python3

import sys
s = [i for i in input().strip()]
c = 0
for i in s:
    if i.isupper(): c+=1
print(c+1)

