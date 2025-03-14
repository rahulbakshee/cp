# linear search - TLE
# time:O(nm), space:O(1), n-len(candies), m-max(candies)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0


        def isAllocationPossible(possible):
            kids = 0
            for i in range(len(candies)):
                kids += candies[i] // possible

            return kids >= k

        left = 1
        right = sum(candies) # 19

        for i in range(sum(candies), -1, -1):
            if isAllocationPossible(i):
                return i
        return 0


# binary search
# time:O(nlogm), space:O(1), n-len(candies), m-max(candies)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0


        def isAllocationPossible(possible):
            kids = 0
            for i in range(len(candies)):
                kids += candies[i] // possible

            return kids >= k

        left = 1
        right = sum(candies) # 19

        while left <= right:
            mid = (left+right)//2

            if isAllocationPossible(mid):
                left = mid+1
            else:
                right = mid-1

        return right
