# Write a function that accepts a traget string and an array of strings
# the function should return a boolean indicating whether or not the taget 
# can be constructed by concatenating elements of the wordbank array
# you may reuse elements of worBank as many times as needed


# recursion
# n-len of wordBank, m-len of target
# time:O(n*m*m), space:O(m)

from typing import List

def canConstruct(target:str, wordBank:List[str])->bool:
	dp = [False] * (len(target)+1)
	dp[0] = True

	for i in range(len(dp)):
		if dp[i]:
			for word in wordBank:
				if target[i:].startswith(word):
					if i+len(word) < len(dp):
						dp[i+len(word)] = True

	return dp[-1]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"])) # False


