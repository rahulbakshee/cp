# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/

# using stack
# time:O(n), space:O(n)
class Solution:
    def getSmallestString(self, s: str) -> str:
        stack = []
        for c in range(len(s)):
            if not stack:
                stack.append(s[c])
            # same parity
            elif int(stack[-1]) % 2 == int(s[c]) % 2:
                # check which is bigger - ab or ba
                if int(stack[-1] + s[c]) > int(s[c] + stack[-1]):
                    temp = stack.pop()
                    stack.append(s[c])
                    stack.append(temp)

                    # return after concatenating with he rest of the string
                    if len(s) > c+1:
                        return str("".join(stack) + s[c+1:])
                    else:
                        return str("".join(stack))

                else:
                    stack.append(s[c])
            else:
                stack.append(s[c])
        return str("".join(stack))


# without stack
# time:O(n), space:O(1)
class Solution:
    def getSmallestString(self, s: str) -> str:
        result = ""
        
        for c in range(len(s)-1):
            prev = int(s[c])
            next = int(s[c+1])

            if prev%2 == next%2 and prev > next:
                s = s[:c] + s[c+1] + s[c] + s[c+2:]
                break
        return s
