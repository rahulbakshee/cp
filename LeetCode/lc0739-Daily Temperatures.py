# solved this by myself on Feb 17, 2025

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([i, temp])
                continue
            
            while stack and temp > stack[-1][1]:
                prev_i, _ = stack.pop()
                result[prev_i] = i-prev_i
                
                
            stack.append([i, temp])
        return result
                
                
                
######################################






# https://leetcode.com/problems/daily-temperatures/description/

# brute force  - O(N**2), space:O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result 


# monotnically decreasing stack
# time:O(n), space:O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #[temp, index]

        for i in range(len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i-stack_index
            stack.append([temperatures[i], i])
                
        return result
