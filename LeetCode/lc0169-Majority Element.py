# https://leetcode.com/problems/majority-element/description/

# sorting
# time -O(n log n), space-O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# hashmap
# time-O(n), space-O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        # loop over dictionary to find key with the max value
        max_key, max_value = 0, 0
        for key in hashmap.keys() :
            if hashmap[key] > max_value:
                max_value = hashmap[key]
                max_key = key
        return max_key


# Moore Voting Algorithm
# time-O(n), space-O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = float("-inf")

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1
            
        return candidate

