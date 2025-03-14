# write a function allConstruct(target, wordBank) that accepts 
# a target string and an array of strings
# Function shoudl return a 2D array containing all of the ways that
# target can be constructred by concatenating elements of the 
# wordBank array.each element of the 2D array should represent one 
# combination that constructs the target.
# you may reuse elements of wordBank as many times as needed


# recursion + memoization
# time:O(n^m), space:O(m)
# n - len of wordBank, m-len of target

from typing import List

def allConstruct(target:str, wordBank:List[str], memo)->List[str]:
	# base case
	if target in memo:
		return memo[target]

	if target == "":
		return [[]]

	result = []
	for word in wordBank:
		if target.startswith(word):
			suffix = target[len(word):]
			suffixWays = allConstruct(suffix, wordBank, memo)

			targetWays = [[word] + suffixWay for suffixWay in suffixWays]
			
			result.extend(targetWays)

	memo[target] = result
	return memo[target]



print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"],{})) # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"],{})) # [['abc', 'def']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"],{})) # []
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"],{})) # []