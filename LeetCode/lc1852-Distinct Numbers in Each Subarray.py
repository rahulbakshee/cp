# time:O(n), space:O(k)
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        result = []

        for i in range(k):
            hashmap[nums[i]] += 1

        result.append(len(hashmap))

        # move the window one element at a time
        for i in range(1, len(nums)-k+1):
            # if the added item is same as removed item
            # then do nothing
            if nums[i-1] != nums[i+k-1]:
                # if not same then update the window hashmap
                # increment 
                hashmap[nums[i+k-1]] += 1
                # decrement
                if hashmap[nums[i-1]] == 1:
                    del hashmap[nums[i-1]]
                else:
                    hashmap[nums[i-1]] -= 1
            
            # keep adding len of hashmap to result
            result.append(len(hashmap))

        return result
