"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler016
Project Euler #16: Power digit sum
"""
#!/bin/python3 


for _ in range(int(input())):
    num = list(str(2**int(input())))
    print(sum([int(x) for x in num]))
    
