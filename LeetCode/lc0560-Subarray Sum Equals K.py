# bruteforce
# time:O(n**2), space:O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        for i in range(len(nums)):
            curr_sum = nums[i]
            if curr_sum == k:
                result += 1
            for j in range(i+1, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    result += 1

        return result



# neetcode solution - REVISE
# time:O(n), space:O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefixSum = {0:1}

        for n in nums:
            curr_sum += n
            diff = curr_sum - k 

            res += prefixSum.get(diff, 0)
            prefixSum[curr_sum] = 1+ prefixSum.get(curr_sum, 0)


        return res



# short and rememeber this
# https://leetcode.com/problems/path-sum-iii/editorial/
class Solution:
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        
        for num in nums:
            # The current prefix sum
            curr_sum += num
            
            # Situation 1:
            # Continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # Situation 2:
            # The number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # Add the current sum
            h[curr_sum] += 1
                
        return count
