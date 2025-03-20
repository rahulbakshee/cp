# time:O(n), space:O(n)
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        total = sum(nums)
        counter = Counter(nums)
        outlier = float("-inf")
        for num in nums:
            curr = total - 2 * num
            if curr in counter:
                if curr != num or counter[num] >1:
                    outlier = max(outlier, curr)    

        return outlier
