# time:O(n^3), space:O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False


