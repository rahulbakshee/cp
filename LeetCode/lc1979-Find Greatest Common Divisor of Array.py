# sorting - time:O(nlogn), space:O(sorting/n)
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[-1]

        # # iterative
        # def gcd(a,b):
        #     while b > 0:
        #         a,b = b, a%b
        #     return a

        # recursive
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        return gcd(a,b)

# single pass - time:O(n), space:O(1)
class Solution:
    def findGCD(self, nums: List[int]) -> int:

        min_num  = max_num = nums[0]
        for num in nums:
            min_num  = min(num, min_num)
            max_num = max(num, max_num)

        # # iterative
        # def gcd(a,b):
        #     while b:
        #         a,b = b, a%b
        #     return a
        
        # recursive
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)
        return gcd(min_num, max_num)
      
