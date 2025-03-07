# Write a function that takes in a targetSum and array of numbers.
# The function should return an array containbing the shortest 
# combination of numbers that add up to exactly the targetSum
# if there is a tie for the shortest combination
# you may return any one of the shortest


# recursion + memoization
# m - targetSum, n-len(nums)
# time:O(m^2*n), space:O(m^2)

from typing import List

def bestSum(targetSum:int, nums:List[int],memo={})->List[int]:
	# base case
	if targetSum in memo:
		return memo[targetSum]

	if targetSum == 0:
		return []

	if targetSum < 0:
		return None

	shortest_combination = None

	for num in nums:
		remainder = targetSum - num
		remainderCombination = bestSum(remainder, nums,memo)
		if remainderCombination is not None:
			curr_combination = remainderCombination + [num]
			if shortest_combination is None or len(curr_combination) < len(shortest_combination):
				shortest_combination = curr_combination


	memo[targetSum] = shortest_combination
	return memo[targetSum]


print(bestSum(7, [5,3,4,7],{})) # [7] 
print(bestSum(8, [2,3,5],{})) # [5,3] 
print(bestSum(8, [1,4,5],{})) #  [4,4]
print(bestSum(100, [1,2,5,25],{})) # [25, 25, 25, 25]
