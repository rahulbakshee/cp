# recursive backtracking - time:O(3^n), space:O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache
        def backtrack(i, open_count):
            # base case
            if i >= len(s):
                return open_count == 0 # all opens sould be closed

            if s[i] == "(":
                return backtrack(i+1, open_count+1)

            elif s[i] == ")":
                if open_count <= 0: # there should be at least one open
                    return False
                return backtrack(i+1, open_count-1)

            else: # s[i] == "*"
                # try all 3 possibilities
                return (backtrack(i+1, open_count) or # treat as ""
                        backtrack(i+1, open_count+1) or # treat as "("
                        backtrack(i+1, open_count-1)) # treat as ")"

        return backtrack(0,0)



"""greedy - time:O(n), space:O(1)
 - Track the possible range of open parentheses ( using two variables:
     - low = minimum number of unmatched '(' (treating * as ') or '')
     - high = maximum number of unmatched '(' (treating * as '(')

 - At each step:
     - If high < 0, it means too many ) → invalid.
     - At the end, low must be 0 for valid string.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        # range of possible open parenthesis counts
        low, high = 0, 0 
        
        for char in s:
            if char == "(":
                low += 1
                high += 1

            elif char == ")":
                low -= 1
                high -= 1

            else: # "*"
                low -= 1    # treat as ")"
                high += 1   # treat as "("

            # too many unmatched ")"
            if high < 0:
                return False

            # can't have negative open count
            if low < 0:
                low = 0

        return low == 0
      
