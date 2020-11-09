"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler006
Project Euler #1: Multiples of 3 and 5
"""
#!/bin/python3

import sys

for _ in range(int(input())):
    n = int(input().strip())
    sum1,sum2 = 0,0
    sum1 += (n*(n+1)//2)**2
    sum2 += n*(n+1)*(2*n+1)//6
    print(abs(sum1-sum2))
