# bruteforce: time limit exceeded
# time:O(n**2), space:O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        args:
            target
            nums

        returns:
            len of mimimal length of subarray whose sum is greater than or equal to target
        """
        n = len(nums)
        min_len = n
        flag = 0

        for i in range(n):
            curr_sum = nums[i]
            if curr_sum >= target:
                min_len = 1
            for j in range(i+1, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(min_len, j-i+1)
                    flag = 1

        return min_len if flag else 0


# two pointers
# time:O(n), space:O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = len(nums)+1

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len<=len(nums) else 0









