# https://leetcode.com/problems/keys-and-rooms/solutions/331847/5-python-solutions/?envType=study-plan-v2&envId=leetcode-75

# DFS - recursive - time:O(n+e), space:O(n), n-rooms, e-keys
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room_index):
            if room_index not in keys:
                keys.add(room_index)
                for i in rooms[room_index]:
                    dfs(i)
        
        keys = set()
        dfs(0)
        return len(keys) == len(rooms)


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
