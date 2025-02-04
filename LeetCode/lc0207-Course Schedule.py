# time:O(V+E), space:O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph problem
        # create graph - course:[prereq1, prereq2,, prereq3.....]
        # explore the courses one by one by exploring their childre(prereqs)
        # if we are able to fully explore all prereqs of a  course then return True
        # else return False
        # cycle - 1:[2,3,1]



        # define dfs
        def dfs(course, gray, balck):
            """ returns True if course can be completed, else False"""
            # add the current course to gray set
            gray.add(course)

            for prereq in graph[course]:
                if prereq in gray:
                    return False
                if prereq in black:
                    continue
                if not dfs(prereq, gray, white):
                    return False

            # remove from gray(currently exploring) to black(fully expored)
            gray.remove(course)
            black.add(course)
            return True

        # create a graph
        from collections import defaultdict
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # graph -  {course1:[prereq1, prereq2,, prereq3.....]}
        
        white = set(graph.keys()) # unexplored
        gray = set() # currently being expored
        black = set() # full explored

        # start exploring courses one by one
        while white:
            course = white.pop()

            # if cycle then return False, else return True
            if not dfs(course, gray, black):
                return False

        return True
