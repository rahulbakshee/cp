class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        blacks = 0

        for ball in s:
            if ball == "0":
                swaps += blacks
            else:
                blacks += 1
        return swaps
