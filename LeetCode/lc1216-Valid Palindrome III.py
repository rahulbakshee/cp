# https://www.youtube.com/watch?v=cJBT7Q106hg&ab_channel=CrackingFAANG

# time:O(n^2), space:O(n^2)
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True



        if not k:
            return isPalindrome(0, len(s)-1)

        memo = {}
        def helper(i,j,k):
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            if k == 0:
                memo[(i,j,k)] = isPalindrome(i,j)
                return memo[(i,j,k)]

            else:
                while i<j:
                    if s[i] != s[j]:
                        memo[(i,j,k)] = helper(i+1,j, k-1) or helper(i, j-1, k-1)
                        return memo[(i,j,k)]
                    i += 1
                    j -= 1

                memo[(i,j,k)] = True
                return memo[(i,j,k)]


        return helper(0,len(s)-1,k)

    
    
