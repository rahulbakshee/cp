# horizontal scanning
# time:O(S) - O(S) , where S is the sum of all characters in all strings., space:O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix



# vertical scanning
# time:O(S) - O(S) , where S is the sum of all characters in all strings., space:O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][:i]

        return strs[0]

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
            
