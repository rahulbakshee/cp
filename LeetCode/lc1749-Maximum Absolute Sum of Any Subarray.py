class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                #print(j)
                curr_sum += nums[j]
                #print("current", curr_sum)

                max_sum = max(max_sum, abs(curr_sum))
                # print("max", max_sum)
        return max_sum


# from editorial
class Solution:
    def maxAbsoluteSum(self, nums):
        min_prefix_sum = float("inf")
        max_prefix_sum = float("-inf")
        prefix_sum = 0
        max_abs_sum = 0

        for num in nums:
            # Prefix sum from index 0 to i
            prefix_sum += num

            # Minimum & Maximum prefix sum we have seen so far
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

            if prefix_sum >= 0:
                # If the prefix_sum is positive, we will get the difference
                # between prefix_sum & min_prefix_sum
                max_abs_sum = max(
                    max_abs_sum, max(prefix_sum, prefix_sum - min_prefix_sum)
                )
            elif prefix_sum <= 0:
                # If the prefix_sum is negative, we will get the absolute difference
                # between prefix_sum & max_prefix_sum
                max_abs_sum = max(
                    max_abs_sum,
                    max(abs(prefix_sum), abs(prefix_sum - max_prefix_sum)),
                )

        return max_abs_sum
