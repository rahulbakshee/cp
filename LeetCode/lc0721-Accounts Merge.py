# time:O(nmlognm), space:O(nm). n-account, m-emails
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    
    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAccount = {} # email -> index of acc
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e in emailToAccount:
                        uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i


        emailGroup = defaultdict(list) # index of acc -> list of emails
        for e, i in emailToAccount.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)


        result = []
        for i, email in emailGroup.items():
            name = accounts[i][0]
            result.append([name] + sorted(emailGroup[i]))

        return result
