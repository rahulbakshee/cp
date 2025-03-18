# Write a function that takes in a targetSum and array of numbers.
# The function should return an array containbing the shortest 
# combination of numbers that add up to exactly the targetSum
# if there is a tie for the shortest combination
# you may return any one of the shortest


# recursion
# m - targetSum, n-len(nums)
# time:O(m*m*n), space:O(m*m)

from typing import List

def bestSum(targetSum:int, nums:List[int])->List[int]:
	dp = [None] * (targetSum+1)
	dp[0] = []

	for i in range(len(dp)):
		if dp[i] is not None:
			for num in nums:
				if i+num < len(dp):
					new_combination = dp[i] + [num]
					if dp[i + num] is None or len(new_combination) < len(dp[i+num]):
						dp[i+num] = new_combination


	return dp[targetSum]

print(bestSum(7, [5,3,4,7])) # [7] 
print(bestSum(8, [2,3,5])) # [5,3] 
print(bestSum(8, [1,4,5])) #  [4,4]
print(bestSum(100, [1,2,5,25])) # [25, 25, 25, 25]
print(bestSum(100, [25, 1,2,4,5])) # [25, 25, 25, 25]

