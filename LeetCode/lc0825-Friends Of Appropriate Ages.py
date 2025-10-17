class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)

        result = 0
        for ageA, countA in counter.items():
            for ageB, countB in counter.items():
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                if ageA < 100 < ageB:
                    continue

                result += countA * countB
                if ageA == ageB:
                    result -= countA

        return result
