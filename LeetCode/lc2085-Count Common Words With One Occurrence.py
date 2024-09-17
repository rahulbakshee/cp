# time:O(n1+n2), space:O(n1+n2)
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word_dict1 = {}
        for word in words1:
            if word in word_dict1:
                word_dict1[word] += 1
            else:
                word_dict1[word] = 1
        word_dict2 = {}
        for word in words2:
            if word in word_dict2:
                word_dict2[word] += 1
            else:
                word_dict2[word] = 1

        result = 0
        for key, val in word_dict1.items():
            if key in word_dict2:
                if val == 1 and word_dict2[key] == 1:
                    result += 1

        return result
