# time:O(nlogn) sorting + O(n*2**n)
# space:O(sorting) + O(2**n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        sol = []

        def backtrack(i):
            # base case
            if i == len(nums):
                result.append(sol.copy())
                return

            # use it
            sol.append(nums[i]) # sol = [1]
            backtrack(i+1)
            sol.pop()

            # don't use it
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return list(result)
