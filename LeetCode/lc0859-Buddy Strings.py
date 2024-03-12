

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # no characters apart from english alphabets
        # no capital letters
        # no empty string
        # how many reults are expected - only one pair of swap elemnts



        # approach - 
        # 1 check lengths of two strings - if not equal then return False
        # 2 loop over the len(string)
        #           match between two stings- count how many differences between elemnets
        #           num of diff should be 2

        # "ab", "aab" - False
        # "ab", "ab" - False
        # "ab", "ba" - 1,2- True
        # "abc", "bac" - 1,2 - True
        # "abcd", "badc" - 1,2,3,4 - count!= 2 - False

        # "aa", "aa" - 

        if len(s) != len(goal):
            return False
        
        if s==goal and len(set(s)) < len(s):
            return True

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
        
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        else:
            return False
