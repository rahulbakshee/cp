class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        curr = []
        for row in range(rowIndex+1):
            curr = []
            for col in range(row+1):
                if col == 0 or col == row:
                    curr.append(1)
                else:
                    val = prev[col-1] + prev[col]
                    curr.append(val)
            prev = curr

        return prev

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
        
#         result = []
#         for row in range(rowIndex+1):
#             temp = []
#             for col in range(row+1):
#                 if col == 0 or col == row:
#                     temp.append(1)
                
#                 else:
#                     val = result[-1][col-1] + result[-1][col] 
#                     temp.append(val)          
                
#             result.append(temp)         
            
#         return result[-1]
            
            
            
"""  row     temp     
  ->  0      1
      1      1 1
      2      1 2 1
      3      1 3 3 1
      4      1 4 6 4 1
            
            result
"""
