# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/


# two for loops - time limit exceeded
# time:O(n**2), space:O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        counter = 0
        #result = []
        MOD = 10**9+7

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] <= target:
                    if j-i>1:
                        counter += 2**(j-i-1)
                    else:
                        counter += 1
                    #result.append([nums[i] , nums[j]])
                    #print(result, counter)
                counter = counter % MOD

        return counter





# two pointers
# time:O(n), space:O(sorting)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        counter = 0
        MOD = 10**9+7

        left, right = 0, len(nums)-1
        while left <=right:
            if nums[left] + nums[right] <= target:
                counter += 2**(right-left)
                left +=1
            else:
                right -= 1
            counter = counter % MOD
        return counter % MOD
