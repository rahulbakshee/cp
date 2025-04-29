class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0,0
        result = 0
        maxx = max(nums)
        counter = 0

        while right < len(nums):
            if nums[right] == maxx:
                counter += 1

            while counter >=k:
                result += len(nums) - right
                # increment left
                if nums[left] == maxx:
                    counter -= 1
                left += 1

            right += 1

        return result
