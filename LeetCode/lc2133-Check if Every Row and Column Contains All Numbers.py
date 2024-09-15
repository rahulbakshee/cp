class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for r in range(n):
            for c in range(n):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                if 1 <= matrix[r][c] <= n:
                    rows[r].add(matrix[r][c])
                    cols[c].add(matrix[r][c])
                else:
                    return False
        return True
