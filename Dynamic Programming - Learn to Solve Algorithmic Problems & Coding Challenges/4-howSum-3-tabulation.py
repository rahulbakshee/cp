# write a function that takes in a targetSum and 
# array of numbers. The function should return an array 
# containing any combination of elemnets that add up to 
# exactly targetSum

# m-targetSum, n-nums len
# time:O(m*m*n), space:O(m*m)


from typing import List

def howSum(targetSum:int, nums:List[int]):
    dp = [None] * (targetSum+1)
    dp[0] = []
    # print(dp)

    for i in range(len(dp)):
        if dp[i] is not None:
            for num in nums:
                if i+num < len(dp):
                    dp[i+num] = dp[i] + [num] 
                    
    return dp[-1]


print(howSum(7, [2,3])) # [3,2,2]
print(howSum(7, [5,3,4,7])) # [4,3]
print(howSum(7, [2,4])) # None
print(howSum(8, [2,3,5])) # [2,2,2,2]
print(howSum(300, [7,14])) # None
