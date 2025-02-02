# time:O(n), space:O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
        
        # check first and last as well
        if nums[0] < nums[-1]:
            count += 1
        return count <=1
