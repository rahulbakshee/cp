""" BFS
 - Early Exit: If starting point "0000" is a deadend, return -1.
 - BFS Initialization:
    - Use a queue starting from "0000" with 0 moves.
    - Treat each lock state as a node.
    - Use visited set that includes deadends,avoid revisiting/hitting deadends.
 - Generate Next States/children: - SEPARATE FUNCTION
    - For each digit, try turning it up and down (mod 10).
    - Enqueue all unvisited next states.
 - Return the number of moves when target is found.
 - If queue is exhausted, return -1."""
# time:O(d^n+m) = O(10,000), space:O(d^n)
# d-digits(0-9),n-wheels(4),m-deadends
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 1- check if starting point in deadends
        if "0000" in deadends:
            return -1

        # 3 - define function to get children of the curr lock
        def get_children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i])+1)%10)
                result.append(lock[:i] + digit + lock[i+1:])

                digit = str((int(lock[i])-1+10)%10)
                result.append(lock[:i] + digit + lock[i+1:])

            return result

        # 2- start a queue
        visited = set(deadends) # club visited & deadends
        q = deque([("0000", 0)]) # lock , turn

        while q:
            lock, turn = q.popleft()

            # if reached target
            if lock == target:
                return turn

            # explore children
            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turn+1))
            
        return -1
