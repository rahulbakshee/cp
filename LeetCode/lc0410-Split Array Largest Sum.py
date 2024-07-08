# https://leetcode.com/problems/split-array-largest-sum/description/

# binary search
# time:O(n log (sum(nums)), space:O(1)
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold)->bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    count += 1
                    total = num
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
