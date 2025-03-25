# based on https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/solutions/6568581/back-and-forth/



class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        time = [0] * len(skill)

        for i in range(len(mana)):
            t = time[0] + mana[i] * skill[0]

            # go forth
            for j in range(1, len(skill)):
                t = max(t , time[j]) + skill[j] * mana[i]

            # go back
            for j in range(len(skill)-1, -1, -1):
                time[j] = t
                t -= mana[i] * skill[j]

        return time[-1]
