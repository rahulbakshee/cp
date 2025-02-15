class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = []
        
        for i in range(len(nums)):
            if i-k<0 and i+k>=len(nums):
                result.append(nums[i])
                
            elif i-k>=0 and i+k<len(nums) and nums[i-k]<nums[i]>nums[i+k]:
                result.append(nums[i])
            
            elif (i-k<0 and nums[i] > nums[i+k]) or (i+k>=len(nums) and nums[i] > nums[i-k]):
                result.append(nums[i])
            
            print(i, result)

        return sum(result)
