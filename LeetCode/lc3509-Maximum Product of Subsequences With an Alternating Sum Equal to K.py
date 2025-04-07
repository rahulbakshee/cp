# # class Solution:
# #     def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
# #         max_product = 0
# #         def dp(index, sol_index, curr_sum, curr_prod, max_prod):
# #             if curr_prod > limit:
# #                 return -1
# #             # if curr_sum > k:
# #             #     return -1
                
# #             if curr_sum == k and curr_prod <= limit:
# #                 return max(curr_prod, max_prod)

# #             if index >= len(nums):
# #                 return -1

# #             # print(index, sol_index, curr_sum, curr_prod, max_prod)
# #             # odd index
# #             if sol_index%2:
# #                 # print("odd")
# #                 val = -1*nums[index]
# #                 # take it
# #                 take = dp(index+1, sol_index+1, curr_sum+val, curr_prod*nums[index], max(max_prod,curr_prod*nums[index]))

# #                 # not take
# #                 not_take = dp(index+1, sol_index, curr_sum, curr_prod, max_prod)
                
# #                 if take != -1 and not_take != -1:
# #                     return max(take, not_take)
# #                 if take == -1 and not_take == -1:
# #                     return -1
# #                 if take == -1:
# #                     return not_take
# #                 if not_take == -1:
# #                     return take


# #             # even index
# #             else:
# #                 # print("even")
# #                 val = nums[index]
# #                 # take it
# #                 take = dp(index+1, sol_index+1, curr_sum+val, curr_prod*nums[index], max(max_prod,curr_prod*nums[index]))

# #                 # not take
# #                 not_take = dp(index+1, sol_index, curr_sum, curr_prod, max_prod)
                
# #                 if take != -1 and not_take != -1:
# #                     return max(take, not_take)
# #                 if take == -1 and not_take == -1:
# #                     return -1
# #                 if take == -1:
# #                     return not_take
# #                 if not_take == -1:
# #                     return take



# #         result = dp(0,0,0,1,1) # index, sol_index, curr_sum, max_prod
# #         if result == -1:
# #             return -1
# #         return result




# class Solution:
#     def maxProduct(self, nums: List[int], k: int, limit: int) -> int:

        
#         def dp(index, sol_index, curr_sum, curr_prod, max_prod):
#             # if curr_prod > limit:
#             #     return -1
#             # if curr_sum > k:
#             #     return -1
                
#             if curr_sum == k and curr_prod <= limit:
#                 return max(curr_prod, max_prod)

#             if index >= len(nums):
#                 return -1

#             # print(index, sol_index, curr_sum, curr_prod, max_prod)
#             # odd index
#             if sol_index%2:
#                 # print("odd")
#                 val = -1*nums[index]
#                 # take it
#                 take = dp(index+1, sol_index+1, curr_sum+val, curr_prod*nums[index], max(max_prod,curr_prod*nums[index]))

#                 # not take
#                 not_take = dp(index+1, sol_index, curr_sum, curr_prod, max_prod)
                
#                 if take != -1 and not_take != -1:
#                     return max(take, not_take)
#                 if take == -1 and not_take == -1:
#                     return -1
#                 if take == -1:
#                     return not_take
#                 if not_take == -1:
#                     return take


#             # even index
#             else:
#                 # print("even")
#                 val = nums[index]
#                 # take it
#                 take = dp(index+1, sol_index+1, curr_sum+val, curr_prod*nums[index], max(max_prod,curr_prod*nums[index]))

#                 # not take
#                 not_take = dp(index+1, sol_index, curr_sum, curr_prod, max_prod)
                
#                 if take != -1 and not_take != -1:
#                     return max(take, not_take)
#                 if take == -1 and not_take == -1:
#                     return -1
#                 if take == -1:
#                     return not_take
#                 if not_take == -1:
#                     return take



#         result = dp(0,0,0,1,1) # index, sol_index, curr_sum, max_prod
#         if result == -1:
#             return -1
#         return result


# class Solution:
#                 val = nums[index]
#                 # take it
#                 take = dp(index+1, sol_index+1, curr_sum+val, curr_prod*nums[index], max(max_prod,curr_prod*nums[index]))

#                 # not take
#                 not_take = dp(index+1, sol_index, curr_sum, curr_prod, max_prod)
                
#                 if take != -1 and not_take != -1:
#                     return max(take, not_take)
#                 if take == -1 and not_take == -1:
#                     return -1
#                 if take == -1:
#                     return not_take
#                 if not_take == -1:
#                     return take



#         result = dp(0,0,0,1,1) # index, sol_index, curr_sum, max_prod
#         if result == -1:
#             return -1
#         return result




class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:

        @cache
        def dp(index, sign, curr_sum, curr_prod, taken):
            if index >= len(nums):
                if curr_sum == k and taken and curr_prod <= limit:
                    return curr_prod
                return -1
    
            # take it
            take = dp(index+1, sign * -1, curr_sum+sign*nums[index], min(limit+1, curr_prod*nums[index]),True)

            # not take
            not_take = dp(index+1, sign, curr_sum, curr_prod, taken)
            
            return max(take, not_take)
            
        result = dp(0,1,0,1, False)
        dp.cache_clear()
        return result
        



























