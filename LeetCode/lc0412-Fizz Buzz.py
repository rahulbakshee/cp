# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list()

        for index in range(1, n+1):
            currStr = ""

            divisible3 = index % 3 ==0
            divisible5 = index % 5 ==0
            

            if divisible3:
                currStr += "Fizz"
            if divisible5:
                currStr += "Buzz"
            if currStr == "":
                currStr += str(index)

            answer.append(currStr)  
        return answer
