class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        result = ""
        for _ in range(4):
            digit = min(num1%10, num2%10, num3%10)
            result += str(digit)
            num1 = num1//10
            num2 = num2//10
            num3 = num3//10
            #print("digit", digit, "result", result)
        #print(int(result))
        return int(result[::-1])
