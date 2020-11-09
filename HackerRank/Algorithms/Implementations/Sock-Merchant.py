'''
https://www.hackerrank.com/challenges/sock-merchant/problem
Author: rbakshee
'''

#!/bin/python3

num_socks = int(input().strip())
colors_list = list(map(int, input().strip().split(' ')))
colors_set = list(set(colors_list))
count = 0
for col in colors_set:
    count += (colors_list.count(col) // 2)
print(count)

