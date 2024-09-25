# time:O(n.m) - n-len of s1, m-len of s2, space:O(n+m)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        # create frequency count of s1
        freq_s1 = Counter(s1)

        # create windows of n1 length and iterate ove s2
        left, right = 0, n1-1
        
        while right < n2:
            freq_s2 = Counter(s2[left:right+1])

            if freq_s1 == freq_s2:
                return True
            else:
                if freq_s2[s2[left]] > 1:
                    freq_s2[s2[left]] -= 1
                else:
                    freq_s2.pop(s2[left])
                if left != right:
                    if freq_s2[s2[right]] > 1:
                        freq_s2[s2[right]] -= 1
                    else:
                        freq_s2.pop(s2[right])

                left += 1
                right += 1

        return False
