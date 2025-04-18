class Solution:
    def countAndSay(self, n: int) -> str:
        
        def process(num:str)->str:
            result = []
            count = 1

            for i in range(1, len(num)):
                if num[i] == num[i-1]:
                    count += 1

                else:
                    result.append(str(count))
                    result.append(num[i-1])
                    count = 1

            result.append(str(count))
            result.append(num[-1])
        
            return "".join(result)
        
        if n==1:
            return "1"

        result = "1"
        
        for _ in range(1, n):
            result = process(result)            

        return result
