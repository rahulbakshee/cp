# kind of cheating - time:O(n), space:O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# kind of cheating - time:O(n), space:O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]




# using stack - time:O(n), space:O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        
        # push to stack
        for char in s:
            stack.append(char)
        # pop from stack and place into the index
        for i in range(len(s)):
            s[i] = stack.pop()

  

# two pointers - time:O(n), space:O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



      
# recursive  - time:O(n), space:O(n)-recursive call stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recurse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                recurse(l+1, r-1)

        recurse(0, len(s)-1)
