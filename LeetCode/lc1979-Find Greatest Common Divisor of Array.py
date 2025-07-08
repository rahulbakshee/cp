# recursive way
# time:O(max(a, b)), space:O(max(a, b))
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        return gcd(min_num, max_num)


# iterative way
# time:O(max(a, b)), space:O(1)
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a

        return gcd(min_num, max_num)
