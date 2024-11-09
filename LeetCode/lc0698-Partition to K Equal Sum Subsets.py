####### EDITORIAL
# tim:O(n*2^n), space:O(n*2^n)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:
            return False

        total_sum = sum(nums)
        target_sum = total_sum //k
        taken = ['0'] * len(nums)

        # sort the array in reverse order
        nums.sort(reverse=True)

        memo = {}

        def backtrack(index:int, count:int, curr_sum:int)->bool:
            taken_str = "".join(taken)

            if count == k-1:
                return True

            if curr_sum > target_sum:
                return False

            if taken_str in memo:
                return memo[taken_str]

            
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count+1, 0)
                return memo[taken_str]

            
            for i in range(index, len(nums)):
                if taken[i] == "0":
                    taken[i] = "1"

                    if backtrack(index+1, count, curr_sum+ nums[i]):
                        return True

                    taken[i] = "0"

            memo[taken_str] = False
            return memo[taken_str]

        return backtrack(0,0,0)
