# https://leetcode.com/problems/missing-number


# space: O(1), time:O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)


# https://leetcode.com/problems/missing-number/solutions/2563887/eight-different-approaches-in-python3/?orderBy=most_votes




# tim:O(n**2), space:O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i not in nums:
                return i
        return n


# time:O(n), space:O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for i in range(n):
            if i not in nums_set:
                return i
        return n


# time:O(nlogn), space:O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i

        return n


# math way
# time:O(n), space:O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

# binary search
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[-1] == n-1:
            return n

        
        left, right = -1, n 
        while left +1 != right:
            mid = (left+right)//2
            if nums[mid] == mid:
                left = mid
            else:
                right = mid

        return right
