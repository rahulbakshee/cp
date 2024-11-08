class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # leftover = money - (a+b) >= 0
        # minimize sum(a,b)

        # 1- brute force - O(n^2), space:O(1)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                leftover = money - prices[i] - prices[j]
                if leftover >= 0:
                    return leftover

        return money
            



        # 2- sorting time:O(nlogn), space:O(n)
        # sort the prices
        # take the first two index = 0,1
        # sum them and subtract from money
        prices.sort()
        leftover = money - prices[0] - prices[1]
        return leftover if leftover >=0 else money


        # 3- Heap - time:O(nlogk), space:O(k)
        k = 2
        maxHeap = []
        for price in prices:
            heapq.heappush(maxHeap, -1*price)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        leftover = money + sum(maxHeap)
        return leftover if leftover>=0 else money


