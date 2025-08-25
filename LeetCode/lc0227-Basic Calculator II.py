# cracking faang
# # using stack - time:O(n), space:O(n)
# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         num = 0
#         prev_op = "+"

#         for i in range(len(s)):
#             if s[i].isdigit():
#                 num = num*10 + int(s[i])

#             if s[i] in ["+","-","*", "/"] or i == len(s)-1:
#                 if prev_op == "+":
#                     stack.append(num)

#                 elif prev_op == "-":
#                     stack.append(-num)

#                 elif prev_op == "*":
#                     stack.append(stack.pop() * num)
                
#                 elif prev_op == "/":
#                     stack.append(int(stack.pop()/num))

#                 prev_op = s[i]
#                 num = 0

#             # print(stack)
#         return sum(stack)



# without using stack - time:O(n), space:O(1)
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        prev, curr, result = 0, 0, 0

        curr_op = "+"

        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1

                i -= 1

                if curr_op == "+":
                    result += curr
                    prev = curr

                elif curr_op == "-":
                    result -= curr
                    prev = -curr

                elif curr_op == "*":
                    result -= prev
                    result += prev * curr
                    prev = prev *curr

                else:
                    result -= prev
                    result += int(prev / curr)
                    prev = int(prev / curr)
                    

                curr = 0
            elif char != " ":
                curr_op = char

            i += 1

        return result
                







