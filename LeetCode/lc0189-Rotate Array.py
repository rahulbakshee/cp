# bruteforce
# time:O(nk), space:O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        for i in range(k):
            prev = nums[-1]
            for j in range(n):
                nums[j], prev = prev, nums[j]


# using reverse 3 times
# time:O(n), space:O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse_string(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


        # reverses the entire array
        left, right = 0, n-1
        reverse_string(nums, left,right)
        
        # reverse the first half of array till k elements
        left, right = 0, k-1
        reverse_string(nums, left,right)

        # reverse the second half of array from kth element to end of array
        left, right = k, n-1
        reverse_string(nums, left,right)
