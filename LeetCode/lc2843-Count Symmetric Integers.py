class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check_symmetry(num:int)->bool:
            num = str(num)
            n = len(num)
            left = sum(list(map(int, num[:n//2])))
            right = sum(list(map(int, num[n//2:])))
            return left == right

        
        def check_len(num:int)->bool:
            return not len(str(num))%2
                
        
        result = 0
        for num in range(low, high+1):
            if check_len(num) and check_symmetry(num):
                result += 1
                # print(num, result)

        return result
