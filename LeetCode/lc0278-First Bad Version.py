# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# bruteforce , Time Limit Exceeded
# space O(1) , time O(n)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        for version in range(1, n+1):
            if isBadVersion(version):
                return version
            
# binary search, coz it is sorted array
# space O(1) , time O(logn)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right-left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid +1  

        return left
