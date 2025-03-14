# Write a function that accepts a traget string and an array of strings
# the function should return a boolean indicating whether or not the taget 
# can be constructed by concatenating elements of the wordbank array
# you may reuse elements of worBank as many times as needed


# recursion
# n-len of wordBank, m-len of target
# time:O(n^m * m), space:O(m^2)

from typing import List

def canConstruct(target:str, wordBank:List[str])->bool:
	# base case
	if target == "":
		return True
	for word in wordBank:
		if target.startswith(word):
			suffix = target[len(word):]
			if canConstruct(suffix, wordBank):
				return True

	return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
# 					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"])) # False


