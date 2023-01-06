# https://leetcode.com/problems/3sum/

# bruteforce - Time Limit Exceeded
# space O(1) time O(n*3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return result


# two pointers
# space O(1) time O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue

            # two pointer
            mid, right = left + 1, len(nums)-1

            while mid < right and left < mid:
                # check for sum
                s = nums[left] + nums[mid] + nums[right]

                if s > 0:
                    right -= 1
                elif s < 0:
                    mid += 1
                else: # s == 0
                    result.append([nums[left] , nums[mid] , nums[right]])
                    # check for duplictaes
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1

        return result


