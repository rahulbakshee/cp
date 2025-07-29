# time:O(mn3^w), m-rows,n-cols,w-max len of words
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]

        curr.endOfWord = True

    def search(self, word:str):
        """we will do search using DFS
           so no need to implement here
        """          


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        dimensions = [(0,1),(1,0),(0,-1),(-1,0)]        

        # board dimensions
        rows = len(board)
        cols = len(board[0])

        result = set()
        visited = set()

        def dfs(r, c, node, word): # curr node in Trie
        # word string being built chr by char
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            if (r,c) in visited:
                return

            if board[r][c] not in node.children:
                return

            visited.add((r,c))

            node = node.children[board[r][c]]

            word += board[r][c]

            if node.endOfWord:
                result.add(word)

            for dr, dc in dimensions:
                new_r = r+dr
                new_c = c+dc
                dfs(new_r, new_c, node, word)

            visited.remove((r,c))
        

        # call dfs
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,trie.root,"")


        return list(result)
