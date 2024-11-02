# tim:O(n), space:O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]



# time:O(n), space:O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        
        # loop over dic and find the num with freq as 1
        for key, val in counter.items():
            if val == 1:
                return key




# time:O(logn), space:O(1)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            is_even = (right-mid) %2 == 0

            if nums[mid] == nums[mid+1]:
                if is_even:
                    left = mid+2
                else:
                    right = mid-1
            elif nums[mid] == nums[mid-1]:
                if is_even:
                    right = mid-2
                else:
                    left = mid+1
            else:
                return nums[mid]

        return nums[left]

