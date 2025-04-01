# DP - plain recursion
# time:O(2^n), space:O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i):
            # check out of bounds
            if i >= len(questions):
                return 0

            # take it 
            points, brainpower = questions[i]
            take = dp(i+brainpower+1)+ points

            # don't take it
            skip = dp(i+1)

            return max(take, skip)

        return dp(0)


# DP -  recursion + memoization
# time:O(n), space:O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i, memo):
            if i in memo:
                return memo[i]

            # check out of bounds
            if i >= len(questions):
                return 0

            # take it 
            points, brainpower = questions[i]
            take = dp(i+brainpower+1, memo) + points

            # don't take it
            skip = dp(i+1, memo)

            memo[i] =  max(take, skip)
            return memo[i]

        return dp(0, {})


# DP - tabulation
# time:O(n), space:O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        # when len of questions is at least 2
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            points, brainpower = questions[i]
            # take
            if i+brainpower+1 < len(dp):
                take = dp[i+brainpower+1] + points 
            else:
                take = points
            
            # skip
            skip = dp[i+1]

            dp[i] = max(take, skip)


        return dp[0]
