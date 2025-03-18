# write a function allConstruct(target, wordBank) that accepts 
# a target string and an array of strings
# Function shoudl return a 2D array containing all of the ways that
# target can be constructred by concatenating elements of the 
# wordBank array.each element of the 2D array should represent one 
# combination that constructs the target.
# you may reuse elements of wordBank as many times as needed


# recursion
# time:O(n^m), space:O(n^m)
# n - len of wordBank, m-len of target

from typing import List

def allConstruct(target:str, wordBank:List[str])->List[str]:
	dp = [[] for _ in range(len(target) + 1)] 
	dp[0] = [[]]

	for i in range(len(dp)):
		if dp[i]:
			for word in wordBank:
				if target[i:].startswith(word):
					if i+len(word) < len(dp):
						new_combination = [comb + [word] for comb in dp[i]]
						dp[i+len(word)].extend(new_combination)

	return dp[-1]



print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # [['abc', 'def']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # []
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
# 					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"])) # []