# time:O(n), space:O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        t_dict = Counter(t)
        window_dict = {}

        have = 0
        need = len(t_dict)

        result, resultLen = [-1,-1], float("inf")
        left = 0

        for right in range(len(s)):
            curr = s[right]
            # add the curr char to window
            if curr in window_dict:
                window_dict[curr] += 1
            else:
                window_dict[curr] = 1

            # check if this curr char is also in t_dict
            if curr in t_dict and window_dict[curr] == t_dict[curr]:
                have += 1

            # check have and need, update window size
            while have == need:
                if (right-left+1) < resultLen:
                    resultLen = right-left+1
                    result = [left, right]

                # pop from left of window
                window_dict[s[left]] -= 1
                if s[left] in t_dict and window_dict[s[left]] < t_dict[s[left]]:
                    have -= 1
                
                # move left pointer
                left += 1

        left, right = result
        return s[left:right+1] if resultLen != float("inf") else ""
