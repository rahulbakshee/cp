# time:O(n), space:O(1)
class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        if int(sqrt(n)) **2 != n:
            return False
        
        counter = 0
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0:
                counter += 1
                if counter > 1:
                    return False
        return counter == 1
