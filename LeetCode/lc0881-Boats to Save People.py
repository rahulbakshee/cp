

# two pointers
# time:O(n), space:O(1)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        
        left, right = 0, len(people)-1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                
            else:
                right -= 1
            boats += 1
        return boats
