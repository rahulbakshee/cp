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
















# time:O(n), space:O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        result.reverse()
        return " ".join(result)


# https://leetcode.com/problems/reverse-words-in-a-string/solutions/172258/python-two-pointers-no-cheating/
class Solution(object):
    def reverseWords(self, s):
        arr = list(s)
        self.reverse_string(arr, 0, len(arr)-1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)


    def reverse_string(self, arr, l, r):
        '''reverse a given string'''
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1 ; r -= 1
        return arr
    
    
    def reverse_word(self, arr):
        '''reverse every words in a string'''
        l, r = 0 , 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace(): r += 1
            self.reverse_string(arr, l, r-1)
            r += 1; l = r
        return arr
    
    def trim_sides(self, arr):
        '''str.strip() basically'''
        if ''.join(arr).isspace(): return []
        l , r = 0, len(arr) - 1
        while l < r and arr[l].isspace(): l += 1
        while l < r and arr[r].isspace(): r -= 1
        return arr[l:r+1]
    
    def trim_space(self, word):
        '''remove duplicating space in a word'''
        if not word: return []
        res = [word[0]]            
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace(): continue
            res.append(word[i])
        return res
