# BFS from editorial
# time:O(n**(h/2)), space:O(n**(h/2))
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i*i for i in range(1, int(n**(0.5)+1))]

        level = 0
        queue = {n}

        while queue:
            level += 1
            next_queue = set()

            for remainder in queue:
                for square_num in square_nums:
                    if remainder < square_num:
                        break
                    elif remainder > square_num:
                        next_queue.add(remainder-square_num)
                    else:
                        return level
            queue = next_queue

        return level




# DP from editorial
# time:O(n.n**1/2), space:O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(n**(0.5))+ 1)]

        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for square_num in square_nums:
                if i < square_num:
                    break
                dp[i] = min(dp[i], dp[i-square_num]+1)

        return dp[n]
