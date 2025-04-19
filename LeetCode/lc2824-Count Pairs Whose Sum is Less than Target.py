# time:O(n^2)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    result += 1

        return result



# sort + two pointers
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] < target:
                count += right-left
                left += 1

            else:
                right -= 1

        return count
