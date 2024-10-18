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
