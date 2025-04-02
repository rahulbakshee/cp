# n^3
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    maxx = max(maxx, (nums[i] - nums[j]) * nums[k])

        return maxx 


# n^2
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                result = max(result, (maxPrefix-nums[j])*nums[k])
                maxPrefix = max(maxPrefix, nums[j])

        return result

# there are O(n) solutions also on editorial page. go check it
