# 1 - bruteforce - time:O(n^2), space:O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)

        for num in nums:
            curr = num
            curr_len = 0
            while curr in nums:
                curr_len += 1
                curr += 1

            max_len = max(max_len, curr_len)

        return max_len

# 2 - sorting
# time:O(nlogn), space:O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()

        counter = 1
        max_counter = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
                
            if nums[i] == nums[i-1]+1:
                counter += 1

            else:
                counter = 1

            max_counter = max(max_counter, counter)

        return max_counter



# 3 - 
# time-O(n), space-O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        
        for num in nums:
            if num-1 not in nums:
                # it is the starting point
                length = 0
                while (num+length) in nums:
                    length += 1
                max_len = max(max_len , length)

        return max_len

# 3-
# time:O(n), space:O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of input nums
        # helpful for constant lookups
        nums_set = set(nums)

        max_counter = 0

        for num in nums_set:
            if num-1 not in nums_set:
                curr_num = num
                counter = 1
                while curr_num+1 in nums_set:
                    curr_num += 1
                    counter += 1

                max_counter = max(max_counter, counter)

        return max_counter


