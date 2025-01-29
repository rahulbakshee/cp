class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        # create a dict for easy lookup
        wordToWord = defaultdict(set)
        for w1, w2 in similarPairs:
            wordToWord[w1].add(w2)
            wordToWord[w2].add(w1)

        for i in range(len(sentence1)):
            if not(sentence1[i] == sentence2[i] or sentence2[i] in wordToWord[sentence1[i]]):
                return False

        return True
# Here, n is the number of words in sentence1 and sentence2 and k is the length of similar pairs. Let m be the average length of words in sentence1 as well as similarPairs.

# Time complexity: O((n+k)⋅m)
# Space complexity: O(k⋅m)
# from editorial
