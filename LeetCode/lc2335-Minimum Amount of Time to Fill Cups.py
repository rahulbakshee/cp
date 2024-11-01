
# time:O(nlogn) - n - len of amount
# space:O(1)
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # sort the input
        amount.sort()

        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        else:
            return (sum(amount)+1)//2





# time:O(nlogn+m*nlogn) - n - len of amount, m is sum of amounts
# space:O(n)
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # sort the input
        amount.sort()

        result = 0
        while amount[0] and amount[1]:
            result += 1
            amount[1] -= 1
            amount[2] -= 1
            amount.sort()

        result += amount[2]

        return result




# time:O((c+h+w)log(c+h+w)) - amounts of cold, hot, warm
# space:O(1)
import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        maxHeap = [-1*amt for amt in amount]
        heapq.heapify(maxHeap)

        result = 0
        # pop latest two amounts from heap
        while maxHeap[0] != 0:
            pop1 = heapq.heappop(maxHeap)
            pop2 = heapq.heappop(maxHeap)

            result += 1
            # push into heap with processed amounts
            if pop1 != 0:
                heapq.heappush(maxHeap, pop1+1)
            else:
                heapq.heappush(maxHeap, pop1)
            if pop2 != 0:
                heapq.heappush(maxHeap, pop2+1)
            else:
                heapq.heappush(maxHeap, pop2)
            
        return result



