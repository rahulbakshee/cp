# time:O(n), space:O(1) if not counting the result str
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        result = ""
        # a bool variable to store if x can be inserted in n
        # true means we inserted x in n
        # false means we need to insert x at the end of n
        flag = False

        # if the number is negative
        if n[0] == "-":
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    flag = True
                    result = n[:i] + str(x) + n[i:]
                    break
        
        # number is positive
        else:
            for i in range(len(n)):
                if int(n[i]) < x:
                    flag = True
                    result = n[:i] + str(x) + n[i:]
                    break

        # check if x should be added at the last position
        if not flag:
            result = n+str(x)
        return result
