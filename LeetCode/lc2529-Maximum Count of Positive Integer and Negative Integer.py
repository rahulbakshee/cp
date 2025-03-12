# time:O(n), space:O(!)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos, neg)



# binary search        
# time:O(n), space:O(!)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def upper_bound(nums):
            left, right = 0, len(nums)-1
            index = len(nums)

            while left <= right:
                mid = (left+right)//2

                if nums[mid] <= 0:
                    left = mid +1
                else:
                    right = mid - 1
                    index = mid
            return index

        def lower_bound(nums):
            left, right = 0, len(nums)-1
            index = len(nums)

            while left <= right:
                mid = (left + right)//2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    index = mid

            return index

        pos = len(nums) - upper_bound(nums)
        neg = lower_bound(nums)

        return max(pos, neg)   
