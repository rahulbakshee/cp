# time:O(n), space:O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_count = 0
        result = 0

        for end in range(len(s)):
            if s[end] in count:
                count[s[end]] += 1
            else:
                count[s[end]] = 1
            
            max_count = max(max_count, count[s[end]])
    
            if end-start+1-max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result


