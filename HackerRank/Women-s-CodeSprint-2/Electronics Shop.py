https://www.hackerrank.com/contests/womens-codesprint-2/challenges/electronics-shop
>user rbakshee

#!/bin/python3

import sys


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = sorted(list(set([int(keyboards_temp) for keyboards_temp in input().strip().split(' ')])))
pendrives = sorted(list(set([int(pendrives_temp) for pendrives_temp in input().strip().split(' ')])))

temp = 0
final = 0
for i in keyboards:
    for j in pendrives:
        if i+j <= s:
            temp = i+j
            if temp>final:
                final = temp
if final != 0: print(final)
else: print(-1)
