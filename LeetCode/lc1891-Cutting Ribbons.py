# time:O(log(max(n))), space:O(1)
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 1
        right = max(ribbons)

        while left <= right:
            mid = left + (right-left)//2
            result = 0
            for ribbon in ribbons:
                result += ribbon // mid

            if result >= k:
                left = mid + 1

            else:
                right = mid-1

        return right

