# REFER EDITORIAL  - 6 methods 

# time:O(n), space:O(n)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def build(curr_index, curr_count, pattern):
            if curr_index != len(pattern):
                if pattern[curr_index] == "I":
                    build(curr_index+1, curr_index+1, pattern)
                else:
                    curr_count = build(curr_index+1, curr_count, pattern)

            result.append(str(curr_count+1))
            return curr_count+1


        if not pattern:
            return ""
        result = []

        build(0,0, pattern)
        
        return "".join(result)[::-1]


# time:O(n), space:O(n)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result= []

        for i in range(len(pattern)+1):
            stack.append(i+1)
            
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    result.append(str(stack.pop()))

        return "".join(result)
