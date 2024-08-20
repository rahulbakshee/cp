# time:O(4**n) - 4 is the max letters asscociated with any digits
# space:O(recursive call stack)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                    }
        result = []
        def backtrack(i, sol):
            # base case
            if len(sol) == len(digits):
                result.append(sol)
                return

            for l in letters[digits[i]]: # "abc"
                backtrack(i+1, sol+l)

        backtrack(0, "")
        return result
