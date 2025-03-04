# time:O(logn base 3), space:O(n)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        memo = set()

        while n>0:
            p = 0
            while 3**p <= n:
                p += 1

            n = n - 3**(p-1)
            if p-1 in memo:
                return False
            memo.add(p-1)
            print(n)

            if n == 0:
                return True
            if n < 0 :
                return False


        return n == 0


# time:O(log n base 3), space:O(1)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = 0
        while 3**p <= n:
            p += 1

        # subtact power of 3
        while n > 0:
            if n >= 3**p:
                n = n - 3**p

            # check if same power could be used
            if n >= 3**p:
                return False

            p -= 1

        return True

            

        
