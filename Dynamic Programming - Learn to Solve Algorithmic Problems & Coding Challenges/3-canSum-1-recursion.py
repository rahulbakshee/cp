# Write a function that takes in a targetSum and arrya of numbers.
# This function returns a boolean indicating whther or not it is 
# ssible to generate the targetSum using numbesrs from the array
# You may use an element from array as many times as you want
# all inputs are non-negative


# m - targetSum, n - len(nums)
# time:O(n^m), space:O(m)

from typing import List

def canSum(targetSum:int, nums:List[int])->bool:
	# base case
	if targetSum < 0:
		return False
	if targetSum == 0:
		return True

	for num in nums:
		remainder = targetSum - num
		if canSum(remainder, nums):
			return True

	return False


print(canSum(7, [2,3])) # True
print(canSum(7, [5,3,4,7])) # True
print(canSum(7, [2,4])) # False
print(canSum(8, [2,3,5])) # True
# print(canSum(300, [7,14])) # False
