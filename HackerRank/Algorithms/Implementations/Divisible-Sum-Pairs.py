'''
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
Author: rbakshee
'''

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
c = 0
for x in range(n):
    for y in range(x+1, n):
        if (a[y]+a[x])%k == 0:
            c += 1
print(c)

