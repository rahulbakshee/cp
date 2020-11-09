"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler008
Project Euler #8: Largest product in a series
"""
#!/bin/python3 

"""
from functools import reduce
from operator import mul

for _ in range(int(input().strip())):
    n,k = map(int, input().strip().split())
    number = int(input())
    num_list = list(str(number))
    newsum, oldsum = 0,0
    for i in range(n-k+1):
        temp = [int(q) for q in num_list[i:i+k]]
        oldsum = reduce(mul, temp, 1)
        if newsum < oldsum:
            newsum = oldsum
    print(newsum)
