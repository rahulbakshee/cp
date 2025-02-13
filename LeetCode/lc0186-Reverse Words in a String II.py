# time:O(n), space:O(1)
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        # helper function for reversing the string
        def reverse_string(strs):
            left, right = 0, len(strs)-1
            while left < right:
                strs[left], strs[right] = strs[right], strs[left]
                left += 1
                right -=1
            return strs

        # helper function to reverse each word
        def reverse_each_word(strs):
            left, right = 0, 0
            while right < len(strs):
                while right < len(strs) and strs[right] != " ":
                    right += 1

                # at this point, strs[right] = " "
                # the string is strs[left:right]
                strs[left:right] = reverse_string(strs[left:right])
                
                # update points
                right += 1
                left = right

            return strs

        # reverse the entire string
        s = reverse_string(s)

        # reverse each word in string
        s = reverse_each_word(s)
