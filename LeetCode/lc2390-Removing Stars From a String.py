class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)



# time:O(n), space:O(1)
class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        i,j = 0,0
        while j<len(s):
            if s[j] == "*":
                if result:
                    result.pop()
                
            else:
                result.append(s[j])

            
            j += 1
            i = j

        return "".join(result)
