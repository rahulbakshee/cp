# https://leetcode.com/problems/climbing-stairs/description/

# recursion - TLE - time limit exceeded
# time-O(2**n), space-O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n

        result = self.climbStairs(n-2)+self.climbStairs(n-1)
        return result


# memoization
# time-O(n), space-O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n:int, memo:dict[int, int])->int:
        if n==1 or n==2:
            return n
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]


# bottom up/Tabulation
# time-O(n), space-O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        bottom_up = [None] * (n+1)
        bottom_up[1] = 1
        bottom_up[2] = 2

        for i in range(3, n+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        return bottom_up[n]

# Space Optimization
# time-O(n), space-O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        
        prev, curr = 1 , 2
        for i in range(3, n+1):
            curr, prev = prev+curr, curr
        return curr
