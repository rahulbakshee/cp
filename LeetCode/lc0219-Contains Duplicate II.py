# https://leetcode.com/problems/contains-duplicate-ii/

# brute force
# space O(1), time O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <=k:
                    return True
        return False

# without using enumerate
# space O(n), time O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()

        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]] - i) <=k :
                    return True
                # update the value
                d[nums[i]] = i
            else:
                d[nums[i]] = i

        return False

# using enumerate
# space O(n), time O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()

        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index

        return False
