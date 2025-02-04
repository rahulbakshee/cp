# time:O(n), space:O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []

        for item in path_list:
            if item == "":
                continue
            elif item == ".":
                continue                
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)            
                
        return "/" + "/".join(stack) if stack else "/"



# https://leetcode.com/discuss/interview-question/6161836/Meta's-Variant-for-Leetcode-71-(Simplify-Path)/

def get_path(cwd, cd):
    
    def simplify(path):
        sub_parts = path.split("/")
        result = []
        for part in sub_parts:
            if part == "." or part == "":
                continue
            elif part == "..":
                if result: result.pop()
            else:
                result.append(part)
        answer = "/".join(result)
        return "/" + answer

    
    if not cd:                  # Case 0
        return simplify(cwd)
    if not cwd:                 # Case 0
        return simplify(cd)
    if cd.startswith("/"):      # Case 1
        return simplify(cd)
    else:                       # Case 2
        return simplify(cwd + "/" + cd)
