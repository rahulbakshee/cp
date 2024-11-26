# cracking fang
# time:O(E+V), space:O(V)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        # step - 1 build the graph
        # graph = {course1: [req1, req2,,,,,]}

        graph = {course:[] for course in range(numCourses)}
        for course, req in prerequisites:
            graph[course].append(req)

        # step 2- create sets which we could use for identifying 
        # white(unexplored), gray(currently being explored), black(fully explored)

        white = set(graph.keys())
        gray = set()
        black = set()
        order = []

        # step 4- define DFS
        def dfs(course, gray, black, order):
            gray.add(course)

            for prereq in graph[course]:
                if prereq in black:
                    continue
                
                if prereq in gray:
                    return False
                    
                if not dfs(prereq, gray, black, order):
                    return False
                
            order.append(course)
            gray.remove(course)
            black.add(course)
            return True

        # step 3 - start exploring from white
        # add them to gray, and start exploring its children/prereq
        # once done, remove it from gray, add it to black once fully explored

        while white:
            course = white.pop()
            
            if course in black:
                continue

            if not dfs(course, gray, black, order):
                return []

        return order

