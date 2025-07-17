# time:O(C)-C is length of all strings in words added together
# time: O(V+E) - Vertex + Edges,  space:O(V+E)
# Topological Sort - DFS cycle detection
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1 - build graph for every character in  very word
        graph = {char:[] for word in words for char in word}

        # 2 - iterate over words list pair by pai
        # try to find if a word is followed by its prefix
        for word1, word2 in zip(words, words[1:]):
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            # iterate over the words and try to find first differentiating char
            # to update the graph
            for i in range(min_len):
                if word1[i] != word2[i]:
                    graph[word2[i]].append(word1[i]) # same as course schedule
                    break                            # course:[dependencies]
                                                     # curr_char:[earlier chars]

        # 3 - run DFS to detect cycle
        # keep updating the order of alphabets
        result = []

        white = set(graph.keys())   # To complete/explore
        black = set()               # already explored/completed nodes
        gray = set()                # currently processing nodes
        
        def dfs(node)->bool:
            if node in black:
                return True
            # check if node is currently bein processed
            if node in gray:
                return False

            # add to gray set/currently processing set
            gray.add(node)

            # explore neighbors
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            # remove from gray and add to black
            gray.remove(node)
            black.add(node)

            # update to result
            result.append(node)

            return True              

        # white -> gray -> black
        while white:
            node = white.pop()
            # check if node already explored
            if node in black:
                continue

            if not dfs(node):
                return ""

        return "".join(result)



# time:(V+E), space:O(V+E)
# Kahn algo - toplogical sort using BFS
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1 - init graph
        graph = {c:set() for word in words for c in word}
        indegree = {c:0 for c in graph}

        # 2 - populate graph and indegree
        for word1, word2 in zip(words, words[1:]):
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for i in range(min_len):
                if word1[i] != word2[i]: # differentiator letter
                    if word2[i] not in graph[word1[i]]:
                        graph[word1[i]].add(word2[i])
                        indegree[word2[i]] += 1
                    break

        
        # 3 - add all the indegree 0 guys to queue
        result = []
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        # start BFS
        while q:
            c = q.popleft()
            result.append(c)
            
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        if len(result) < len(graph):
            return ""
        return "".join(result)
