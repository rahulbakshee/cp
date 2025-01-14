# time:O(s), space:O(s)
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        curr_num = 0
        curr_str = ""
        stack = []

        while i < len(s):
            # if number
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0
            elif s[i] == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str                
            else:
                curr_str += s[i]

            i += 1

        return curr_str


# time:O(n), space:O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)

            else:
                curr_str = ""
                # keep on popping from stack until "["
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str

                # pop to remove "["
                stack.pop()

                # try to get the number
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)
