# time:O(n), space:(1)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalks = sum(chalk)

        remaining = k % chalks

        for i in range(len(chalk)):
            if remaining < chalk[i]:
                return i
            remaining = remaining - chalk[i]

# binary search, time:O(n + logn) -> O(n), space:O(n)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [None] * len(chalk)
        prefix[0] = chalk[0]
        for c in range(1, len(chalk)):
            prefix[c] = prefix[c-1] + chalk[c]

        remaining = k % sum(chalk)

        left, right = 0, len(prefix)-1
        while left < right:
            mid = left + (right-left)//2
            if prefix[mid] <= remaining:
                left = mid +1
            else:
                right = mid

        return left
