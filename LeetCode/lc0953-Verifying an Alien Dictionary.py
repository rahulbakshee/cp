# time:O(all chars in input words), space:O(order_to_num)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_to_num = {}
        for num, letter in enumerate(order):
            order_to_num[letter] = num

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_to_num[word1[j]] > order_to_num[word2[j]]:
                        return False
                    break
        return True
                
