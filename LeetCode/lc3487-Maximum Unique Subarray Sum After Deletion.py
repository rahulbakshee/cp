class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)
        result = 0
        for num in nums:
            if num > 0:
                result += num
            else:
                if result == 0:
                    result += num
                    break

        return result
