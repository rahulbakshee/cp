# time:O(n^2), space:O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        max_sum = 0
        for i in range(len(nums)):
            curr_sum = nums[i]
            j = i+1
            while j< len(nums) and nums[j] > nums[j-1]:
                curr_sum += nums[j]
                j += 1

            max_sum = max(max_sum, curr_sum)

        return max_sum



# time:O(n), space:O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        max_sum = 0
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0
            curr_sum += nums[i]

        return max(max_sum, curr_sum)
