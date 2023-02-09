# https://leetcode.com/problems/ugly-number

# space : O(1), time: O(logn)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        def isDivisible(number, divisor):
            if number % divisor == 0:
                return True
            else:
                return False

        
        for d in [2,3,5]:
            if isDivisible(n, d):
                while isDivisible(n, d):
                    n = n // d
            
        if n ==1:
            return True
        else:
            return False
