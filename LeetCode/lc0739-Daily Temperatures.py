# bruteforce - time:O(n^2), space:O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result



# monotnically decreasing stack - time:O(n), space:O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])
                continue

            while stack and temp > stack[-1][0]:
                _, index = stack.pop()
                result[index] = i-index
                # number of days you have to wait after the ith day
            
            stack.append([temp,i])

        return result
                
