# https://leetcode.com/problems/container-with-most-water/description/

# bruteforce- time-O(n**2), space-O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                
                area = max(area, min(height[i], height[j]) * (j-i))
                #print(height[i], height[j], area)

        return area


# two pointer- time-O(n), space-O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height)-1, 0

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area


