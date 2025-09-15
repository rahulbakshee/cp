# with stack
# # time:O(n), space:O(n)
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         stack = [] # to store all the opening brackets "("
#         indexes_to_remove = set()

#         for i, char in enumerate(s):
#             if char not in "()":
#                 continue
#             elif char == "(":
#                 stack.append(i)
#             else: # ")"
#                 if not stack:
#                     indexes_to_remove.add(i)
#                 else:
#                     stack.pop()

#         indexes_to_remove = set(stack).union(indexes_to_remove)
#         result = []
#         for i in range(len(s)):
#             if i not in indexes_to_remove:
#                 result.append(s[i])

#         return "".join(result)


# without stack
# time:O(n), space:O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_s = list(s)
        counter = 0

        # iterate ove the input to process "(" and ")"
        for i, char in enumerate(list_s):
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1

            # if at any moment more closing than opening brackets
            # then remove the current char ")" and incement the counter.
            if counter < 0:
                list_s[i] = ""
                counter += 1

        # if we have more opening than closing
        # iterate right to left and fix/remove the first opening bracket 
        # and decrement the counter
        if counter > 0:
            for i in range(len(list_s)-1,-1,-1):
                if list_s[i] == "(":
                    list_s[i] = ""
                    counter -= 1
                
                # if at any moment the counter is zero come out of the loop
                if counter == 0:
                    break

        return "".join(list_s)



# neetcode

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        balance = 0

        # pass 1
        for char in s:
            if char == "(":
                result.append(char)
                balance += 1

            elif char == ")":
                if balance > 0:
                    result.append(char)
                    balance -= 1
            else:
                result.append(char)


        # pass 2 - fron end to start
        filtered = []
        for char in result[::-1]:
            if char == "(" and balance >0:
                balance -= 1

            else:
                filtered.append(char)

        return "".join(filtered[::-1])


