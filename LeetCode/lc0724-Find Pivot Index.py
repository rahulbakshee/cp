# time:O(n), space:O(n)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [None] * len(nums)
        left_sum[0] = 0

        right_sum = [None] * len(nums)
        right_sum[-1] = 0


        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]

        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        
        return -1


# time:O(n), space:O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        sum_nums = sum(nums)

        for i in range(len(nums)):
            if left_sum == sum_nums - left_sum - nums[i]:
                return i

            # update left_sum
            left_sum += nums[i]

        return -1
