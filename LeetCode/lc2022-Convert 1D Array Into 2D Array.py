# time:O(m*n)
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        result = [[0]*n for _ in range(m)]

        index = 0
        for i in range(m):
            for j in range(n):
                result[i][j] = original[index]
                index += 1
            
        return result
                
# time:O(m*n)
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        result = [[0]*n for _ in range(m)]

        for i in range(len(original)):
            row, col = divmod(i, n)
            result[row][col] = original[i]
    
            
        return result
                
