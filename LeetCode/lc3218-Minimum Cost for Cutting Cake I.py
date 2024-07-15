# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

# time:O(n logn), space:O(n)
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        hori = sorted(horizontalCut)
        verti = sorted(verticalCut)
        sum_hori =sum(hori)
        sum_verti = sum(verti)
        result = 0

        while hori and verti:
            if hori[-1] > verti[-1]:
                result += hori[-1] + sum_verti
                h = hori.pop()
                sum_hori -= h
            else:
                result += verti[-1] + sum_hori
                v = verti.pop()
                sum_verti -= v

        return result + sum_hori + sum_verti
