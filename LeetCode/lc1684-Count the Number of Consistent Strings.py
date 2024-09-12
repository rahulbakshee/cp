# time:O(a+w*n) - n is len of list words, w is avg len of each word, a is len of allowed
# space:O(a+w)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        def is_consistent(set_allowed, word):
            set_word = set(word)
           
            for key in set_word:
                if key not in set_allowed:
                    return False
            
            return True

        count = 0
        set_allowed = set(allowed)
        for word in words:
            if is_consistent(set_allowed, word):
                count += 1
        return count
