"""“I’m familiar with both DFS and BFS-based approaches for topological sort.
DFS is great when I want to detect cycles explicitly or explore dependencies 
recursively, while BFS using Kahn’s Algorithm is better for iterative processing, 
especially if I want to construct a valid course order or handle large input without
recursion issues.”"""
# TOPOLOGICAL SORT - DFS detect cycles
# time:O(V+E), space:O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1- build the graph
        # graph = {course1:[pre1, pre2], course2:[], course3:[pre5]....}
        graph = {course:[] for course in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)

        # 2- define three variables to store completed, 
        gray = set()    # currently completing
        white = set(graph.keys())   # to be completed
        black = set()   # completed

        # 3- define DFS
        def dfs(course, gray, black):
            gray.add(course)

            # explore children/prereqs
            for prereq in graph[course]:
                if prereq in black:
                    continue
                if prereq in gray: # cycle
                    return False

                if not dfs(prereq, gray, black):
                    return False
            # remove course from gray and add to black
            gray.remove(course)
            black.add(course)            
            return True


        # 4- call DFS on evry course and their children/prereqs. 
        # if successful return True, else False
        while white:
            course = white.pop()
            if not dfs(course, gray, black):
                return False

        return True

# Kahn's Algorithm (BFS Topological Sort)
# time:O(V+E), space:O(V+E)
"""
 - Build the graph (adjacency list) and indegree map:
     - graph[a] contains all courses that depend on a.
     - indegree[b] counts how many prerequisites course b has.
 - Initialize a queue with all courses having indegree == 0 (i.e., no prerequisites).
 - Process the queue:
    - Pop a course c, and count it as completed.
    - For each neighbor of c in the graph, decrement its indegree.
    - If any neighbor’s indegree becomes 0, add it to the queue.
 - Check if all courses are completed:
    - If the number of processed courses equals numCourses, return True.
    - Otherwise, a cycle exists → return False."""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 1-build indegree map and graph
        indegree = [0] * numCourses
        
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest) # course src->dest
            indegree[dest] += 1     # increment indegree of dest 

        # queue of courses with no prereqs (0 indegree)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # run bfs - topological sort
        completed = 0
        while queue:
            node = queue.popleft()
            completed += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                # if indegree is 0 add it to q
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
                    
