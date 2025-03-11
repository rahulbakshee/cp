# time:O(n), space:O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        def has_all_chars(freq):
            return all(f>0 for f in freq)
        
        n = len(s)
        left, right = 0, 0
        result = 0
        freq = [0] * 3

        while right < n:
            freq[ord(s[right]) - ord("a")] += 1

            # check if all 3 elements in window/freq
            while has_all_chars(freq):
                result += n-right
                
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return result

