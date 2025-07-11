""" make order_dict and compare adjacent words
 - Map Alien Order to Indices:
     - Create a dictionary to map each character to its position in the alien 
        alphabet (e.g., 'h' → 0, 'l' → 1, etc.).
     - This allows O(1) lookups for character comparisons.

 - Compare Adjacent Words:
     - Iterate through the list of words, comparing each pair of adjacent 
     words (words[i] and words[i+1]).
     - For each pair, find the first differing character and verify their 
     order based on the alien dictionary.
     - If all characters match, the longer word must come after the shorter
      one (e.g., "apple" should come after "app").
 - Return Result:
     - If all adjacent pairs are correctly ordered, return True.
     - If any pair violates the order, return False.
"""
# time:O(nm) -  n-len of words array, m-avg word length
# space:O(1) - 26 chars of english
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # build order dict - {"a":1,"b":2,"c":3....}
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i

        # compare adjacent words
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                # check if word2 was prefix of word1
                # we reached end of w2 before w1
                if j == len(word2):
                    return False

                # find first differing character
                if word1[j] != word2[j]:
                    # check if ordering correct
                    if order_dict[word2[j]] < order_dict[word1[j]]: 
                        return False

                    break # dont need to compare rest of chars
                    # dont return False, just break out of loop

        return True
