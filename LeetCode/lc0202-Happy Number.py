# https://leetcode.com/problems/happy-number/description/

# time:O(), space:O()
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visit = set()

        while n not in visit:
            visit.add(n)

            n = self.sum_of_sq_of_digits(n)

            if n==1:
                return True
        return False
    
    def sum_of_sq_of_digits(self, n:int)->int:
        output = 0
        
        while n:
            digit = n % 10
            output += digit **2
            n = n //10
        return output
            
