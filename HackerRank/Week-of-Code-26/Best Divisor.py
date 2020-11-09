"""
https://www.hackerrank.com/contests/w26/challenges/best-divisor
"""
#!/bin/python3

import sys

n = int(input().strip())

div_list = []

#get the list of all divisors including that number
for i in range(1, n+1):
    if n%i == 0:
        div_list.append(i)


past_number = 9999999
past_sum = 0

for x in div_list:
    bump = list(str(x))
    new_sum = sum([int(k) for k in bump])
    if new_sum == past_sum:
        best = min(past_number, x)
    else:
        if new_sum > past_sum:
            best = x
        else:
            best = past_number
    past_sum = new_sum
    past_number = x
    #print("x", x)
    #print("new_sum", new_sum)
    #print("past_sum", past_sum)
    #print("best", best)
print(best)
