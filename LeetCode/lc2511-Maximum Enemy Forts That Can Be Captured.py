# time:O(n), space:O(1)
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
        def process(forts):
            result = 0
            for f in range(len(forts)):
                if forts[f] == 1:
                    index = f+1
                    while index < len(forts) and forts[index] == 0:
                        index += 1

                    if index != len(forts) and forts[index] == -1:
                        result = max(result, index-f-1)


            return result
        
        # from left to right
        result1 = process(forts)
        print(result1)
        # from right to left
        result2 = process(forts[::-1])
        print(result2)
        return max(result1, result2)
