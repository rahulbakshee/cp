# https://leetcode.com/problems/water-bottles/description/

# time:O(n), space:O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        result += numBottles
        empty = numBottles
        while empty >= numExchange:
            result += int(empty // numExchange)
            empty = int(empty // numExchange) + int(empty % numExchange)
            # print("result", result, "empty", empty)
        return result
