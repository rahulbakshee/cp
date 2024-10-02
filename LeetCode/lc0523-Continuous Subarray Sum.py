# time:O(n**2), space:O(1)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i+1, len(nums)):
                curr_sum += nums[j]
                if curr_sum%k == 0:
                    return True

        return False


# neetcode video
# time:O(n), space:O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            rem = total % k
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] > 1:
                return True

        return False
