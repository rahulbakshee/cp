# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        prev = -1
        for wealth in accounts:
            if sum(wealth) > prev:
                prev = sum(wealth)
            
        return prev
