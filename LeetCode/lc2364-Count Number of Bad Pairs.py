# time:O(n), space:O(n)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        hashmap = {}
        for i in range(len(nums)):
            diff = i - nums[i]

            good_pairs = hashmap.get(diff, 0)

            bad_pairs += i - good_pairs

            hashmap[diff] = good_pairs + 1
            
        return bad_pairs


# time:O(n), space:O(n)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)-1
        total = n*(n+1)//2

        good = 0
        memo = {}

        for i in range(len(nums)):
            diff = i-nums[i]
            good += memo.get(diff, 0)
            memo[diff] = memo.get(diff, 0) + 1

        return total - good
