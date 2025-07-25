class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        curr = "1"

        for _ in range(1, n):
            next_term = ""
            i = 0

            while i < len(curr):
                count = 1
                while i+1 < len(curr) and curr[i] == curr[i+1]:
                    count += 1
                    i += 1

                # append count and digit to the next term
                next_term += str(count) + curr[i]
                i += 1
            curr = next_term

        return curr

#########################################


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
