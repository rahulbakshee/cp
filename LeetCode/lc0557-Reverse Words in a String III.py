# time:O(n), space:O(1)
class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse_string(strs):
            left, right = 0, len(strs)-1
            while left < right:
                strs[left], strs[right] = strs[right], strs[left]
                
                left += 1
                right -= 1
        
            return strs

        def reverse_each_word(strs):
            left, right = 0,0
            while right < len(strs):
                while right < len(strs) and strs[right] != " ":
                    right += 1
                print("right", right)
                strs[left:right] = reverse_string(strs[left:right])

                right += 1
                left = right

            return strs
        
        # convert string into list
        l = list(s)
        
        # reverse each word in list
        l = reverse_each_word(l)
        
        return "".join(l)
