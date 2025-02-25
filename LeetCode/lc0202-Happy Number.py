# using hashset
# time:O(logn), space:O(logn)
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def happy(n):
            result = 0
            while n:
                remainder = n%10
                n = n//10
                result += remainder **2

            return result
            
        seen = set()
        while n != 1 and n != 4:
            seen.add(n)
            n = happy(n)
        
        return n==1


########################
# using Floyd cycle detection algo
# time:(logn), space:O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def happy(n):
            result = 0
            while n:
                remainder = n%10
                n = n//10
                result += remainder **2

            return result
            

        slow = n
        fast = happy(n)
        while fast != 1 and slow != fast:
            slow = happy(slow)
            fast = happy(happy(fast))
        
        return fast==1
