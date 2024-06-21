# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# sliding window - time:O(n), space:O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()

        for right in range(len(s)):
            if s[right] not in seen: # new char
                seen.add(s[right])
                max_len = max(max_len, right -left + 1)

            else: # repeat char - remove the initial chars till the current char
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])

        return max_len
