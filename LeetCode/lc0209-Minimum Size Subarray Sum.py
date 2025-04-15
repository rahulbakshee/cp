# bruteforce: time limit exceeded
# time:O(n**2), space:O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n
        flag = 0

        for i in range(n):
            curr_sum = nums[i]
            if curr_sum >= target:
                min_len = 1
            for j in range(i+1, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(min_len, j-i+1)
                    flag = 1

        return min_len if flag else 0

# two pointer
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n+1
        curr_sum = 0

        left, right = 0,0
        while right < n:
            curr_sum += nums[right]

            # if curr_sum exceeds the target, reduce 
            # the window size by incremnting left
            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
                
            right += 1

        return min_len if min_len!=n+1 else 0
        


"""
target = 7
nums = [2,3,1,2,4,3]

left index = 0, 1, 2
right index = 0, 1, 2, 3, 4

curr_sum = 7

min_len = 4



"""





# two pointers
# time:O(n), space:O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        subarr_sum = 0

        for right in range(len(nums)):
            subarr_sum += nums[right]
            while subarr_sum >= target:
                result = min(result, right-left+1)
            
                # move window
                subarr_sum -= nums[left]
                left += 1

        return 0 if result == float("inf") else result




