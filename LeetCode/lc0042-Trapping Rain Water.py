# https://leetcode.com/problems/trapping-rain-water/description/

# creating two arrays - leftMax and rightMax which hold the max values till now
# time-O(n), space-O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0]*n, [0]*n

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        total_trapped = 0
        for i in range(n):
            trapped = min(maxLeft[i], maxRight[i]) - height[i]
            if trapped > 0:
                total_trapped += trapped

        return total_trapped


# using two pointers - leftMax and rightMax which hold the max values till now
# time-O(n), space-O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        left, right = 0, n-1
        maxLeft, maxRight = height[left], height[right]
        trapped = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                trapped += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                trapped += maxRight - height[right]
        return trapped



