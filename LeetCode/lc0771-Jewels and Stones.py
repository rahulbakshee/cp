class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)
        hashmap_stones = Counter(stones)
        
        
        count = 0
        for key, value in hashmap_stones.items():
            if key in set_jewels:
                count += value
                
        return count
