# time:O(n), space:O(n)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_A, set_B = set(), set()

        count = 0
        result = []

        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
            else:
                set_A.add(A[i])
                set_B.add(B[i])

                if A[i] in set_B:
                    count += 1
                if B[i] in set_A:
                    count += 1

            result.append(count)

        return result
