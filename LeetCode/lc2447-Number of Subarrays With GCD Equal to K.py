# time:O(n**2), space:O(1)
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # iterative
        def gcd(a,b):
            while b>0:
                a,b = b,a%b
            return a


        count = 0
        for i in range(len(nums)):
            temp_gcd = 0
            for j in range(i, len(nums)):
                temp_gcd = gcd(temp_gcd, nums[j])

                if temp_gcd == k:
                    count += 1
                elif temp_gcd <k:
                    break

        return count
