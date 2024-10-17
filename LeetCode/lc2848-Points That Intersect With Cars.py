# time:O(nlogn), space:O(n)
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        result = [nums[0]]
        count = 0

        for i in range(1, len(nums)):
            if nums[i][0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], nums[i][0])
                result[-1][1] = max(result[-1][1], nums[i][1])
            else:
                result.append(nums[i])

        for res in result:
            count += res[1] - res[0] + 1
        return count 
