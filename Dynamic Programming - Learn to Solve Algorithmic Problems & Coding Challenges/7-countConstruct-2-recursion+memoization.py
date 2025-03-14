# write a function countConstruct(target, wordBank) that accepts 
# a target string and an array of strings
# Function shoudl return number of ways that
# target can be constructred by concatenating elements of the 
# wordBank array.
# you may reuse elements of wordBank as many times as needed



# recursion + memoization
# time:O(n * m^2), space:O(m^2)
# n - len of wordBank, m-len of target

from typing import List

def countConstruct(target:str, wordBank:List[str],memo)->int:
	# base case
	if target in memo:
		return memo[target]

	if target == "":
		return 1

	total_count = 0
	for word in wordBank:
		if target.startswith(word):
			suffix = target[len(word):]
			count = countConstruct(suffix, wordBank, memo)
			total_count += count

	memo[target] = total_count
	return memo[target]



print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"],{})) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"],{})) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"],{})) # 0
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
					["e", "ee", "eee", "eeeeeeee", "eeeeeeeeeeeeeeeee"],{})) # 0
