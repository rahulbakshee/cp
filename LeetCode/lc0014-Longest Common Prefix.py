# time: best case - O(k*n) - k is the len of common prefix, n is the len of strs
# time - worst case :O(m*n) - m is len of each str in case of equal length strings, n-len of strs
# space:O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_word = strs[0]
        for i in range(len(first_word)):
            for next_word in strs[1:]:
                if i == len(next_word) or  next_word[i] != first_word[i]:
                    return first_word[:i]

        return first_word


# using trie
#time:O(k*n)
# space:O(k*n)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str)->None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True

    def search(self, main_word:str, search_word:str, search_till_index:int)->int:
        curr = self.root

        search_till_index = min(search_till_index, len(search_word))
        for w in range(search_till_index):
            if search_word[w] not in curr.children or search_word[w]!=main_word[w]:
                return w
            else:                
                curr = curr.children[search_word[w]]

        return search_till_index

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        # insert
        for word in strs[1:]:
            trie.insert(word)

        # search
        search_till = len(strs[0])

        for s in strs[1:]:
            if search_till > 0:
                search_till = trie.search(main_word=strs[0], search_word=s, search_till_index=search_till)
            else:
                return ""

        return strs[0][:search_till]
            
