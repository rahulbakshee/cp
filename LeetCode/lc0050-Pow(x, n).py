# linear
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        for i in range(abs(n)):
            result = result * x

        if n < 0:
            return 1/result
        else:
            return result 





# divide and conquer
# time:O(logn), space:O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            # base case
            if x == 0:
                return 0
            if x == 1:
                return 1
            if n == 0:
                return 1
            if n == 1:
                return x

            result = recurse(x, n//2) # (2, 1)
            result = result * result # 4
            # if n is odd
            if n % 2 == 1:
                return result * x
            else: # n is even
                return result

        result = recurse(x, abs(n))
        if n < 0:
            return 1/ result
        else:
            return result

# x = 2, n = 2 -> 4
# x = 2, n = -2 -> 1/4
# x = 2, n = 3 -> 
