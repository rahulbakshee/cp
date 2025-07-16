# DFS - topological sort
# time:O(V + E), space:O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [course for course in range(numCourses)]

        # 1 - build the graph
        # graph = {course1:[pre1, pre3], course2:[], course3:[pre6].....}
        graph = {course:[] for course in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)

        # 2 - initialize dict for storing the nodes
        gray = set()                # currently processing courses
        white = set(graph.keys())   # to be completed courses
        black = set()               # completed courses

        # 3- start with white set(untouched/to be completed courses) and then explore its preReqs
        # by passing them to DFS, and then marking them completed
        def dfs(course):
            gray.add(course)

            # start exploring its neighbors/preReq
            for nei in graph[course]:
                if nei in gray: # currently preocessing
                    return False

                if nei in black: # already completed
                    continue

                if not dfs(nei):
                    return False

            result.append(course)
            # remove from gray set
            gray.remove(course)
            # add to black set
            black.add(course)

            return True


        result = []
        while white:
            course = white.pop()
            if course in black:
                continue
            if not dfs(course):
                return []

        return result if len(result) == numCourses else []


# Kahn algo - BFS - topological sort
# time:O(V + E), space:O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        graph = {course:[] for course in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1 #REMEMBER

        # queue those who have no prereqs
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # run bfs
        completed = []
        while q:
            course = q.popleft()
            completed.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        
        if len(completed) == numCourses:
            return completed
        return []
