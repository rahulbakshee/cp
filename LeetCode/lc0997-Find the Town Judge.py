# two dicts
# time:O(T+n), space:O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_trust_dict = defaultdict(int)
        out_trust_dict = defaultdict(int)

        for t in trust:
            out_trust_dict[t[0]] += 1
            in_trust_dict[t[1]] += 1

        for i in range(1, n+1):
            if in_trust_dict[i] == n-1 and out_trust_dict[i] == 0:
                return i

        return -1        

# single dict
# time:O(T+n), space:O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_dict = defaultdict(int)
        for t in trust:
            trust_dict[t[0]] -= 1
            trust_dict[t[1]] += 1

        for i in range(1, n+1):
            if trust_dict[i] == n-1:
                return i
        return -1
        
