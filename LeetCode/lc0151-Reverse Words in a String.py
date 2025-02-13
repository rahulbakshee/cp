# time:O(n), space:O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # helper function to reverse a string
        def reverse_string(strs):
            left, right = 0, len(strs)-1
            while left < right:
                strs[left], strs[right] = strs[right], strs[left]
                left += 1
                right-= 1
            return strs
        
        
        # helper function to remove leading, trailing, and concurrent spaces
        def remove_spaces(strs):
            
            left, right = 0, len(strs)-1
            
            # leading spaces
            while left <= right and strs[left] == " ":
                left += 1

            # trailing spaces
            while left<=right and strs[right] == " ":
                right -= 1

            # concurrent spaces
            output = []
            while left <=right:
                if s[left] == " ":
                    if output and output[-1] == " ":
                        left += 1
                        continue
                    else:
                        output.append(s[left])
                else:
                    output.append(s[left])

                left += 1
            return output

        # helper function to reverse each word
        def reverse_each_word(strs):
            left, right = 0,0
            while left < len(strs):
                while right < len(strs) and strs[right] != " ":
                    right += 1
                # reverse the word
                strs[left:right] = reverse_string(strs[left:right])
                left = right + 1
                right += 1

            return strs

        l = list(s)
        l = remove_spaces(l)
        l = reverse_string(l)
        l = reverse_each_word(l)

        return "".join(l)
