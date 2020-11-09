  
"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
Project Euler #1: Multiples of 3 and 5
"""
#!/bin/python3 

import sys

for _ in range(int(input().strip())):
    n = int(input().strip())
    def calc(n,k):
        m = (n-1)//k
        return k*m*(m+1)//2
    print(calc(n,3) + calc(n,5) - calc(n,15))
