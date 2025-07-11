"""track how many people trust each person (incoming) and how many 
people each person trusts (outgoing). The judge must have n-1 
incoming trusts and 0 outgoing trusts."""
# time:O(E+V), space:O(V)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # build two graphs of trusts
        incoming  = defaultdict(int)
        outgoing = defaultdict(int)

        for u, v in trust:
            outgoing[u] += 1
            incoming[v] += 1

        # check for n-1 incoming and 0 outgoing
        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i

        return -1
