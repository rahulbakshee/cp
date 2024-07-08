# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

# simulation with list
# time:O(n**2) one for while loop and one for pop(shifting of array), space:O(n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]

        start = 0

        while len(friends) > 1:
            to_drop = (start + k -1) % len(friends)
            friends.pop(to_drop)
            start = to_drop
        return friends[0]


# simulation with queue
# time:O(n*k) - n for while loop and k for removing/rotating the queue, space:O(n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque(range(1, n+1))

        while len(friends) > 1:
            for i in range(k-1):
                friends.append(friends.popleft())
            friends.popleft()
        return friends[0]


# recrursion and iterative solutions - visit again after few days
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/
