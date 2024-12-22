# time:O(n^2), space:O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        for i in range(len(nums)-k+1):
            curr_sum = 0
            for j in range(i, i+k):
                curr_sum += nums[j]

            max_avg = max(max_avg, curr_sum/k)

        return max_avg

# # time:O(n^2), space:O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        
        for i in range(len(nums)-k+1):
            max_avg = max(max_avg, sum(nums[i:i+k])/k)

        return max_avg


# sliding window
# time:O(n), space:O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_avg = window/k

        for i in range(len(nums)-k):
            window = window - nums[i] + nums[i+k]
            max_avg = max(max_avg, window/k)

        return max_avg

# cumulative sum
# time:O(n), space:O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cum_sum = 0
        for i in range(k):
            cum_sum += nums[i]

        result = cum_sum
        for i in range(k, len(nums)): 
            cum_sum += nums[i] - nums[i-k]
            result = max(result, cum_sum)
        
        return result/k
