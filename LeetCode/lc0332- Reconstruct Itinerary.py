# time:O(ElogE), space:O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # 1- build adj list with reverse input
        graph = defaultdict(list)
        for src, dest in sorted(tickets)[::-1]:
            graph[src].append(dest)


        # 2-
        result = []

        def dfs(src):
            while graph[src]:
                dest = graph[src].pop()
                dfs(dest)
            
            result.append(src)

        dfs("JFK")
        return result[::-1]    


# TIME LIMIT EXCEEDED
# recursive DFS-time:O(V*E), space:O(V*E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 0 - sort input tickets
        tickets.sort()
        
        # 1 - build adjacency list
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)

        # 2- define dfs to traverse over destinations from source
        def dfs(src):
            # REMEMBER len(result) == len(tickets)+1
            if len(result) == len(tickets)+1:
                return True

            # check if you can only go to source not come back
            if src not in graph:
                return False

            # explore neighbors by modifying the adj list
            # drop dest one by one and again push them back to adj list
            temp = list(graph[src])
            for i, v in enumerate(temp):
                graph[src].pop(i)
                result.append(v)

                if dfs(v):
                    return True

                graph[src].insert(i, v)
                result.pop()

            return False

        # 3- call ddfs from "JFK"
        result = ["JFK"]
        dfs("JFK")
        return result
