# better neetcode solution

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 1

        if n == 1:
            return True

        for i in range(1, n*2):
            if nums[(i-1)%n] <= nums[i%n]:
                count += 1
            else:
                count = 1

            if count == n:
                return True


        return False

######################################### use above

# time:O(n), space:O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
        
        # check first and last as well
        if nums[0] < nums[-1]:
            count += 1
        return count <=1
