# time:O(nlogn), space:O(n/sorting)
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)

        total_skill = skill[0] + skill[-1]
        chemistry = 0

        left, right = 0, n-1
        while left < right:
            if skill[left] + skill[right] == total_skill:
                chemistry += skill[left] * skill[right]
            else:
                return -1

            left += 1
            right-= 1
        
        return chemistry
