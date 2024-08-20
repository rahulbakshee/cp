class Solution:
    def fib(self, n: int) -> int:
        if n  == 1 or n == 0:
            return n
        return self.fib(n-1) + self.fib(n-2)


class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def memo(n):
            # base case
            if n == 0 or n== 1:
                return n

            if n in cache:
                return cache[n]
            
            cache[n] = memo(n-1) + memo(n-2)
            return cache[n]

        return memo(n)
