# nested loops, time:O(n^2), space:O(1)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] == -1:
                    continue
                if nums[i] + nums[j] == k:
                    count += 1
                    nums[i] = -1
                    nums[j] = -1
                    break

        return count



# sorting + two poinmters
# time:O(nlogn), space:O(sorting)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] > k:
                right -=1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                left += 1
                right -= 1
                count += 1
        return count
