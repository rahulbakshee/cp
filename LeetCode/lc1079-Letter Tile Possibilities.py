# time:O(n!), space:O(n)
from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def backtrack(counter):
            sol = 0

            for key, value in counter.items():
                if value > 0:
                    # take it
                    counter[key] -= 1
                    sol += 1
                    sol += backtrack(counter)

                    # don't take it
                    counter[key] += 1

            return sol

        return backtrack(Counter(tiles))
