'''
https://www.hackerrank.com/challenges/apple-and-orange
Author: rbakshee
'''

#!/bin/python3

import sys

home_s, home_t = map(int, input().strip().split())
tree_a, tree_b = map(int, input().strip().split())
m_apples, n_oranges = map(int, input().strip().split())
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

count_a = 0
count_o = 0

for a in apple:
    if ((tree_a+a) >= home_s ) and ((tree_a+a) <= home_t ) :
        count_a += 1
for oran in orange:
    if ((tree_b+oran) >= home_s ) and ((tree_b+oran) <= home_t ) :
        count_o += 1


print(count_a)
print(count_o)
        
