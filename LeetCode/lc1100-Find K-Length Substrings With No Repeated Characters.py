
# sliding window
# timeLO(n), space:O(n)
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        freq = set()
        result = 0

        left,right = 0, 0
        while right < len(s):
            while left < len(s) and s[right] in freq:
                freq.remove(s[left])
                left += 1
            
            freq.add(s[right])

            # check for window len > k
            if right-left+1 > k:
                left += 1

            # check for window len = k
            if right - left + 1 == k:
                # print(s[left:right+1])
                result += 1
                freq.remove(s[left])
                left +=1


            right += 1

        return result   
