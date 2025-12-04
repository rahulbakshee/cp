# https://youtu.be/quSfR-uwkZU
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n1 = len(s1)
        n2 = len(s2)

        counter_s1 = [0] * 26
        counter_s2 = [0] * 26

        # build the counter for s1
        for i in range(n1):
            counter_s1[ord(s1[i]) - ord("a")] += 1
            counter_s2[ord(s2[i]) - ord("a")] += 1

        if counter_s1 == counter_s2:
                return True

        # use sliding window to compare between elemnets of window 
        # (counter_s2) with the counter_s1

        for i in range(n1, n2):
            counter_s2[ord(s2[i]) - ord("a")] += 1
            counter_s2[ord(s2[i-n1]) - ord("a")] -= 1

            # compare the two
            if counter_s1 == counter_s2:
                return True

        return counter_s1 == counter_s2
