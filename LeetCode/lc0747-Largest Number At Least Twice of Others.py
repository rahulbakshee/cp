# time:O(n), space:O(1)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxx = max(nums)
        index = nums.index(maxx)

        for i in range(len(nums)):
            if nums[i] == maxx:
                continue
            if nums[i] > maxx//2:
                return -1

        return index
