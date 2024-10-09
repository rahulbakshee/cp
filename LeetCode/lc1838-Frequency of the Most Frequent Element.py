# time:O(nlogn), space:O(sorting)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        max_window = 0
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            window = right-left+1
            if (nums[right] * (window)) - total <= k:
                max_window = max(max_window, window)
                continue
            else:
                total -= nums[left]
                left += 1
        return max_window
