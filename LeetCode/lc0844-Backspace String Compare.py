# https://leetcode.com/problems/backspace-string-compare/description/

# # time:O(s+t), space:O(s+t)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspacing(s:str):
            left = 0
            new_s = []
            while left < len(s):
                if s[left] != "#":
                    new_s.append(s[left])
                else:
                    if new_s:
                        new_s.pop()
                left += 1
            return new_s


        new_s = backspacing(s)
        new_t = backspacing(t)

        return new_s == new_t









import itertools

# copied from editorial - need to revisit
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def do_backspace(s):
            skip = 0
            for c in reversed(s):
                if c == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c
        return all(x == y for x, y in itertools.zip_longest(do_backspace(s), do_backspace(t)))
