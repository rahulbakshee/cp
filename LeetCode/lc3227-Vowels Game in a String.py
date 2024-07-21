# https://leetcode.com/problems/vowels-game-in-a-string/description/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}

        for c in s:
            if c in vowels:
                return True
        return False
