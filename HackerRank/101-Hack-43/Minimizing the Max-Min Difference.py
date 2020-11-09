https://www.hackerrank.com/contests/101hack43/challenges/max-min-difference
user rbakshee


#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = sorted(a)

print( min(abs(a[-1] - a[1]) , abs(a[0] - a[-2])))   

