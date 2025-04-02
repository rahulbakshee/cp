# time:O(m+n), lens of two lists, space:O(m+n)-output space
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        result = []
        f, s = 0,0
        while f<len(firstList) and s<len(secondList):
            startf, endf = firstList[f]
            starts, ends = secondList[s]

            lo = max(startf, starts)
            hi = min(endf, ends)

            if lo <= hi: # there is intersection
                result.append([lo,hi])

            # update indexes
            if endf < ends:
                f += 1
            else:
                s += 1

        return result
