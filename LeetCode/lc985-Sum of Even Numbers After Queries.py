# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        curr_sum = sum([num for num in nums if num%2 == 0])
        output = []
        
        for val, indx in queries:
            
            prev = nums[indx]
            nums[indx]  = nums[indx] + val
            new = nums[indx]
            
            if new %2 == 0 and prev%2 == 0: # if new=even, prev=even
                curr_sum += val
                
            if new %2 == 0 and prev%2 != 0: # if new=even, prev=odd
                curr_sum += new
                
            if new %2 != 0 and prev%2 == 0: # if new=odd, prev=even
                curr_sum -= prev
                
            else: # if new=odd, prev=odd
                pass
               
            #print(prev, nums[indx], nums, curr_sum)
            
            
            output.append(curr_sum)
            
        return output
