# time:O(n^2), space:O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum


# kadane algo
# time:O(n), space:O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum



# kadane- easy to follow =
# time:O(n), space:O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float("-inf")

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num

            maxSum = max(maxSum, currSum)

        return maxSum
