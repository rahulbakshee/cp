# time:O(nlogn) - n is len of num, space:O(n)
class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(str(num))

        evens = sorted([n for n in num if int(n)%2 == 0], reverse=True)
        odds =  sorted([n for n in num if int(n)%2 == 1], reverse=True)

        # print(evens, odds)
        e, o = 0,0

        result = []
        for i in range(len(num)):
            # odd
            if int(num[i]) % 2:
                result.append(odds[o])
                o += 1
            # even
            else:
                result.append(evens[e])
                e += 1        
        
        return int("".join(result))
