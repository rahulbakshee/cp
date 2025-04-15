# time:O(n^2), space:O(1)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_size = 0

        for i in range(n):
            curr_sum = nums[i]
            if curr_sum == k:
                max_size = max(max_size, 1)            
            
            for j in range(i+1,n):
                
                curr_sum += nums[j]
                
                if curr_sum == k:
                    max_size = max(max_size, j-i+1)

        return max_size


# prefix sum
# time:O(n), space:O(n)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = 0
        max_len = 0
        hashmap = {}


        for i in range(n):
            prefix += nums[i]

            if prefix == k:
                max_len = i+1

            if prefix - k in hashmap:
                max_len = max(max_len, i-hashmap[prefix-k])

            if prefix not in hashmap:
                hashmap[prefix] = i

        return max_len 
