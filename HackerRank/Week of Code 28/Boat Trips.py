# https://www.hackerrank.com/contests/w28/challenges/boat-trip
# Author : Rahul Bakshee


#!/bin/python3
import sys


n,c,m = input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = list(map(int, input().strip().split(' ')))
#print("max", max(p))
if  max(p) <= m*c:
    print("Yes")
else:
    print("No")
