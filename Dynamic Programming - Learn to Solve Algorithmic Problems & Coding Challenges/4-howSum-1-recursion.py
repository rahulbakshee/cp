# write a function that takes in a targetSum and 
# array of numbers. The function should return an array 
# containing any combination of elemnets that add up to 
# exactly targetSum

# m-targetSum, n-nums len
# time:O(m * n^m), space:O(m)


from typing import List

def howSum(targetSum:int, nums:List[int]):
    # base case 1
    if targetSum  == 0:
        return []

    # base case 2
    if targetSum < 0:
        return 


    for num in nums:
        remainder = targetSum - num
        remainder_result = howSum(remainder, nums)
        if remainder_result is not None:
            return remainder_result + [num]

     



print(howSum(7, [2,3])) # [3,2,2]
print(howSum(7, [5,3,4,7])) # [4,3]
print(howSum(7, [2,4])) # None
print(howSum(8, [2,3,5])) # [2,2,2,2]
# print(howSum(300, [7,14])) # None
