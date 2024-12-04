# time:O(C)-C is length of all strings in words added together
# O(V+E) - Vertex + Edges
# total time:O(C+V+E)

# space:O(V+E)

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for char in word:
                graph[char] = []

        #print(graph)
        
        # build the graph
        for word1, word2 in zip(words, words[1:]):
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                    return ""
            
            for i in range(minLen):
                if word1[i] != word2[i]:
                    graph[word2[i]].append(word1[i])
                    break

                

        # define dfs
        def dfs(white, gray, black, node, result):
            # add to gray
            gray.add(node)

            for parent in graph[node]:
                # check if in black
                if parent in black:
                    continue
                
                # check if in gray
                if parent in gray:
                    return False
                
                if not dfs(white, gray, black, parent, result):
                    return False
            

            # move node from gray to parent as it is fully explored
            gray.remove(node)
            black.add(node)
            result.append(node)
            return True

        # use three sets
        white = set(graph.keys())
        gray = set()
        black = set()
        result = []

        # start moving nodes from white to gray to black
        while white:
            node = white.pop()
            if node in black:
                continue
            if not dfs(white, gray, black, node, result): # False-if cycle
                return ""

        return "".join(result)
