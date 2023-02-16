# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum

# space: O(1), time O(n)
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        avg = total//3


        counter = 0
        running_sum = 0

        for a in arr:
            running_sum += a
            if running_sum == avg:
                counter += 1
                running_sum = 0
        return counter >= 3