# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# time:O(n**2), space:O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest = 1

        for i in range(len(s)):
            curr_length = 1
            seen = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    curr_length += 1
            longest = max(longest, curr_length)

        return longest



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
