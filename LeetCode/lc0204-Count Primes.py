# https://leetcode.com/problems/count-primes/description/
# Sieve of Eratosthenes 

# time:O( sqrt(n)log(logn) ), space:O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=1:
            return 0
        primes = [1 for i in range(n)]
        primes[0] = 0
        primes[1] = 0

        for i in range(2, int(n**(0.5))+1 ):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)
