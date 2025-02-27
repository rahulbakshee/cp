# Time complexity:  O(n∗m), space:O(1), only 26 char in english
# Where  n is the number of words and m is the average length of a word.
# neetcode

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # build the order dict {char:index}
        order_dict = dict() # {"h":0, "l":1......"z":25}
        for index, char in enumerate(order):
            order_dict[char] = index

        # words = ["abc", "def", "hij","jkl"]
        # ["abc", "def"]
        # ["def", "hij"]
        # ["hij","jkl"]
        
        
        for word1, word2 in zip(words, words[1:]):
            for i in range(len(word1)):
                # check for if i in range of word2
                if i == len(word2):
                    return False

                # first occurence of divergence
                if word1[i] != word2[i]:
                    # check the order of the divergent char
                    if order_dict[word1[i]] > order_dict[word2[i]]:
                        return False
                
                    break

                else:
                    continue

        return True
