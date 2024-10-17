# time:O(max(abbr, word)), space:O(1)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        abbr_i = 0
        word_i = 0

        while abbr_i < len(abbr) and word_i < len(word):
            # alphabet
            if (ord("a") <= ord(abbr[abbr_i]) <= ord("z")):
                if abbr[abbr_i] != word[word_i]:
                    return False
                else:
                    abbr_i += 1
                    word_i += 1
                    continue
            
            # number
            else:
                if abbr[abbr_i] == "0":
                    return False
                num = 0
                while abbr_i < len(abbr) and ord("0")<= ord(abbr[abbr_i]) <= ord("9"):
                    num = int(abbr[abbr_i]) + num*10
                    abbr_i += 1

                word_i += num
            
            print(abbr_i, word_i, num)
        print(abbr_i, word_i)
        return abbr_i==len(abbr) and word_i==len(word)
