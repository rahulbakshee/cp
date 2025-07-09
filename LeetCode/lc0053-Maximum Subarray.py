# kadane- easy to follow = - NEETCODE
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


# bruteforce
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

# DP - bottom up - INTERVIEW
# Store the max subarray sum ending at each index in a dp[] array.
# time:O(n), space:O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            max_sum = max(max_sum, dp[i])

        return max_sum

# kadane algorithm - INTERVIEW
# Track the current maximum subarray sum ending at index i, 
# and the global maximum seen so far. If adding the current 
# element decreases the sum, start a new subarray.
# time:O(n), space:O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

# divide and conquer approach REMAINING
