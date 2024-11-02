# time:O(a+b+c), space:O(1) not counting string builder
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        curr_a = curr_b = curr_c = 0
        total_chars = a+b+c
        result = []

        for _ in range(total_chars):
            if (a>=b and a>=c and curr_a!=2) or (a>0 and (curr_b==2 or curr_c==2)):
                result.append("a")
                a -= 1
                curr_a += 1
                curr_b = 0
                curr_c = 0

            elif (b>=c and b>=a and curr_b!=2) or (b>0 and (curr_a==2 or curr_c==2)):
                result.append("b")
                b -= 1
                curr_b += 1
                curr_a = 0
                curr_c = 0

            elif (c>=a and c>=b and curr_c!=2) or (c>0 and (curr_a==2 or curr_b==2)):
                result.append("c")
                c -= 1
                curr_c += 1
                curr_a = 0
                curr_b = 0

        return "".join(result)





# using heap
# time:O(a+b+c), space:O(1)

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a>0:
            heapq.heappush(maxHeap, [-1*a, "a"])
        if b>0:
            heapq.heappush(maxHeap, [-1*b, "b"])
        if c>0:
            heapq.heappush(maxHeap, [-1*c, "c"])

        # input = [1,1,7]
        #          a,b,c
        # maxHeap = [-7,"a"], [-1,"b"], [-1,"c"]

        result = []
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(result)>=2 and result[-1]== char and result[-2] == char:
                if not maxHeap:
                    break
                tempCount, tempChar = heapq.heappop(maxHeap)
                result.append(tempChar)
                tempCount += 1
                if tempCount < 0:
                    heapq.heappush(maxHeap, [tempCount, tempChar])

            else:
                result.append(char)
                count += 1
                
            if count<0:
                heapq.heappush(maxHeap, [count, char])

        return "".join(result)
