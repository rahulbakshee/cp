# time:O(n**2), space:O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        n= len(mat)
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n-1:
                    result += mat[i][j]

        return result


# time:O(n), space:O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        n= len(mat)
        for i in range(n):
            result += mat[i][i]
            result += mat[n-1-i][i]

        if n%2:
            result -= mat[n//2][n//2]

        return result
