"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler002
Project Euler #2: Even Fibonacci numbers
"""
#python3


for _ in range(int(input().strip())):
    n = int(input().strip())
    a = b = 1
    arr = []
    s = 0
    while b<n:
        arr.append(b)
        b,a = a+b, b
    for k in arr:
        if k%2 == 0: s+= k
    print(s)
