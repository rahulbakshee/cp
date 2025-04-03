# time:O(n^3), space:O(1)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    result = max(result, (nums[i] - nums[j]) * nums[k])

        return result


# time:O(n^2), space:O(1)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        for k in range(2, len(nums)):
            m = nums[0]
            for j in range(1, k):
                result = max(result, (m - nums[j]) * nums[k])
                m = max(m, nums[j])

        return result



# time:O(n), space:O(1)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        imax = 0
        dmax = 0

        for k in range(len(nums)):
            result = max(result, dmax*nums[k])
            dmax = max(dmax, imax-nums[k])
            imax = max(imax, nums[k])

        return result
