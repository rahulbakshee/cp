# https://leetcode.com/problems/defanging-an-ip-address/description/

# space: O(1), time :O(n)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        result = []
        for s in address:
            if s  == ".":
                result.append("[.]")
            else:
                result.append(s)

        return "".join(result)
        