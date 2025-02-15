# from neetcode
# time:O(10^4), space:O(10^4)
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 3- define helper function to get children of parent lock
        def get_children(lock):

            # "0000"
            result = []
            for i in range(4):
                # forward turn
                digit = str((int(lock[i]) + 1)%10)
                result.append(lock[:i] + digit + lock[i+1:])
                
                # backward turn
                digit = str((int(lock[i]) - 1 + 10) %10)
                result.append(lock[:i] + digit + lock[i+1:])
                
            return result
        
    
        # 1 - check if input inbounds
        if "0000" in deadends:
            return -1
    
        # 2 - otherwise initiate a deque
        q = deque()
        q.append(["0000", 0]) # [lock] = "0000"
        visited = set(deadends)

        
        # BFS
        while q:

            lock, turn = q.popleft()
            if lock == target:
                return turn
            
            for child in get_children(lock): # ["0001", "0010"......8]
                if child not in visited:
                    visited.add(child)
                    q.append([child, turn+1])
            
            
        return -1
