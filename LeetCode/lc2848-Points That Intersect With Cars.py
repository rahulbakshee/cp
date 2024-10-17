# time:O(nlogn), space:O(n)
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # sort the input array
        nums.sort()

        # see the result array with first interval
        result = [nums[0]]

        count = 0

        # pass 1- check the newer range with the exsting range
        for i in range(1, len(nums)):
            # overlapping
            if nums[i][0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], nums[i][0])
                result[-1][1] = max(result[-1][1], nums[i][1])
            else:
                # not overlapping
                result.append(nums[i])

        # pass 2- to count the points in the ranges
        for res in result:
            count += res[1] - res[0] + 1
        return count 
