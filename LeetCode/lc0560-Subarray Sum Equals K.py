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
