# time:O(n1 + n2), space:O(n1+n2)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_dict = {}
        for word in s1.split():
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        for word in s2.split():
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        result = []
        for key, val in word_dict.items():
            if val ==1:
                result.append(key)

        return result
