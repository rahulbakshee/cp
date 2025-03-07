# recursion
# time:O(2^n), space:O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def dp(number):
            # base case
            if number == 0:
                return 0
            if number == 1:
                return counter[1]
            
            # take the current numbr
            gain_if_take_current = counter[number]+ dp(number - 2)

            # skip the current number
            gain_if_skip_current = dp(number-1)

            return max(gain_if_take_current, gain_if_skip_current)

        counter = defaultdict(int)
        for num in nums:
            counter[num] += num
        return dp(max(nums))



# recursion + memoization
# time:O(n+k), space:O(n)
# Given N as the length of nums and k as the maximum element in nums,
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def dp(number, memo):
            # base case
            if number == 0:
                return 0
            if number == 1:
                return counter[1]
            if number in memo:
                return memo[number]
            
            # take the current numbr
            gain_if_take_current = counter[number]+ dp(number - 2,memo)

            # skip the current number
            gain_if_skip_current = dp(number-1,memo)

            memo[number] = max(gain_if_take_current, gain_if_skip_current)
            return memo[number]

        counter = defaultdict(int)
        for num in nums:
            counter[num] += num
        return dp(max(nums), {})




# bottom -up - tabulation
# time:O(n), space:O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        counter = defaultdict(int)
        for num in nums:
            counter[num] += num

        dp = [0] * (max(nums)+1)
        dp[1] = counter[1]

        for i in range(2, len(dp)):
            dp[i] = max(counter[i]+dp[i-2], dp[i-1])

        return dp[-1]




# bottom -up - space optimized
# time:O(n), space:O(1)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        counter = defaultdict(int)
        for num in nums:
            counter[num] += num

        prev = 0
        curr = counter[1]

        for i in range(2, max(nums)+1):
            curr, prev = max(counter[i]+prev, curr), curr

        return curr
