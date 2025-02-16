class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()

        result = 0
        n = len(pizzas)
        total_days = n//4

        even_days = total_days//2
        odd_days = total_days - even_days

        for _ in range(odd_days):
            result += pizzas.pop()
        
        
        for _ in range(even_days):
            pizzas.pop()
            result += pizzas.pop()
        
    
        return result
