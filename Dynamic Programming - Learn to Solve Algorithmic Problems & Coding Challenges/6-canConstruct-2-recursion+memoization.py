# Write a function that accepts a traget string and an array of strings
# the function should return a boolean indicating whether or not the taget 
# can be constructed by concatenating elements of the wordbank array
# you may reuse elements of worBank as many times as needed


# recursion + memoization
# n-len of wordBank, m-len of target
# time:O(n * m^2), space:O(m^2)

from typing import List

def canConstruct(target:str, wordBank:List[str],memo={})->bool:
	# base case
	if target in memo:
		return memo[target]

	if target == "":
		return True
	for word in wordBank:
		if target.startswith(word):
			suffix = target[len(word):]
			if canConstruct(suffix, wordBank,memo):
				memo[target] = True
				return memo[target]

	memo[target] = False
	return memo[target]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"],{})) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"],{})) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"],{})) # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"],{})) # False


