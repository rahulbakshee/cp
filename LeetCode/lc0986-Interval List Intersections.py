class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        result = []
        p1, p2 = 0, 0

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start1 > end2:
                p2 += 1
            elif start2 > end1:
                p1 += 1
            else:
                result.append([max(start1, start2), min(end1, end2)])

                # move the pointers - 
                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1

        return result


# l1- [4, 8]
# l2- [2, 5]
# intersection- [max(starts), min(ends)]
