class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniques = len(set(nums))
        hashmap = dict()
        result = 0

        left = 0
        for right in range(len(nums)):
            hashmap[nums[right]] = 1+hashmap.get(nums[right], 0)

            while len(hashmap) == uniques:
                result += len(nums) - right
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1    
                
        return result

