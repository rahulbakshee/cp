# time:O(mn), space:O(1)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        hashmap = defaultdict(int)

        for r in range(rows):
            for c in range(cols):
                hashmap[mat[r][c]] += 1

                if hashmap[mat[r][c]] == rows:
                    return mat[r][c]

        return -1
