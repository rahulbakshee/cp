# time:O(n), space:O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0,1
        result = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if num < 0:
                result[neg] = num
                neg += 2

            else:
                result[pos] = num
                pos += 2

        return result









# # VERY SLOW - DONT USE
# # time:O(n), space:O(n)
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         # indexes where nums[pos] is positive and nums[neg] is negative number
#         pos, neg = 0,0 
        
#         # the write index for result
#         index = 0 
#         result = []

#         while index < len(nums):
#             # move pos index to the positive number
#             while pos< len(nums) and nums[pos] <0 :
#                 pos += 1

#             # move neg index to the negative number
#             while neg<len(nums) and nums[neg] >0:
#                 neg += 1

#             # compare and append to the result
#             # keep moving respective indexes
#             if (not result) or (result and result[-1] < 0):
#                 result.append(nums[pos])
#                 pos += 1    
            
#             else:
#                 result.append(nums[neg])
#                 neg += 1
            
#             index += 1

#         return result


