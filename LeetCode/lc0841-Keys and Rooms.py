# DFS - recursive - time:O(n+e), space:O(n), n-rooms, e-keys
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(key):
            if key not in visited:
                visited.add(key)
                for k in rooms[key]:
                    dfs(k)
                
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)


# DFS - iterative - stack
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]

        while stack:
            key = stack.pop()
            if key not in visited:
                visited.add(key)
                stack.extend(rooms[key])

        return len(visited) == len(rooms)


# BFS - iterative - queue
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        from collections import deque
        q = deque([0])

        while q:
            key = q.popleft()
            if key not in visited:
                visited.add(key)
                for room in rooms[key]:
                    q.append(room)

        return len(visited) == len(rooms)
