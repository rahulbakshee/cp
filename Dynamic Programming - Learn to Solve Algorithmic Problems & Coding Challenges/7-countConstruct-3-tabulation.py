# write a function countConstruct(target, wordBank) that accepts 
# a target string and an array of strings
# Function shoudl return number of ways that
# target can be constructred by concatenating elements of the 
# wordBank array.
# you may reuse elements of wordBank as many times as needed



# recursion
# time:O(m*m*n), space:O(m)
# n - len of wordBank, m-len of target

from typing import List

def countConstruct(target:str, wordBank:List[str])->int:
	dp = [0] * (len(target)+1)
	dp[0] = 1

	for i in range(len(dp)):
		for word in wordBank:
			if target[i:].startswith(word):
				if i+len(word) < len(dp):
					dp[i+len(word)] += dp[i]


	return dp[-1]




print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"])) # 0
