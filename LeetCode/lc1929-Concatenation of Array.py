class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] *len(nums)*2
        n = len(nums)
        for i in range(len(nums)*2):
            if i >= n:
                ans[i] = nums[i-n]
            else:
                ans[i] = nums[i]

        return ans


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        
        for _ in range(2):
            for i in range(n):
                ans.append(nums[i])
        return ans
