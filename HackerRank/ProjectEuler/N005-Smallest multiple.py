"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler005
Project Euler #5: Smallest multiple
"""

#python3

ep=[0,1,2,6,12,60,60,420,840,2520,2520,27720,27720,360360]
T=int(input())
for t in range(T):
    N=int(input())
    print(ep[N])
