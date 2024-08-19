# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         result = []
#         for i in range(numRows):
#             if i == 0:
#                 prev = [1]
#                 result.append(prev)
#                 continue
            
#             curr = [1]
#             j = 1
#             while j < i:
#                 curr.append(prev[j-1] + prev[j])
#                 j+= 1
#             curr.append(1)
#             result.append(curr)
#             prev = curr
#         return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            temp = []
            for col in range(row+1):
                if col == 0 or col == row:
                    temp.append(1)
                
                else:
                    val = result[-1][col-1] + result[-1][col] 
                    temp.append(val)          
                
            result.append(temp)         
            
        return result
            
            
