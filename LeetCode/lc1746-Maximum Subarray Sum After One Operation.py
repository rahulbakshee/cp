# kadane algo
# time:O(n), space:O(1)
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        with_op = without_op = result = float("-inf")

        for n in nums:
            with_op = max(without_op+n**2, with_op+n, n**2)
            without_op = max(without_op+n, n)
            result = max(with_op, without_op, result)

        return result
