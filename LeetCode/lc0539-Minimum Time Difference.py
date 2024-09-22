# time:O(nlogn), space:O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hr, mn = map(int, time.split(":"))
            minutes.append(hr*60+mn)

        minutes.sort()
        print(minutes)
        min_diff = float("inf")
        for i in range(len(minutes)-1):
            min_diff = min(min_diff, minutes[i+1]-minutes[i])

        return min(min_diff, 24*60-(minutes[-1]-minutes[0]))


# time:O(n), space:O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * (24*60)

        for time in timePoints:
            hr, mn = map(int, time.split(":"))
            curr = hr*60+mn
            if minutes[curr]:
                return 0
            minutes[curr] = True

        prev = float("inf")
        first = float("inf")
        last = float("inf")
        min_diff = float("inf")

        for i in range(24*60):
            if minutes[i]:
                if prev!= float("inf"):
                    min_diff = min(min_diff, i-prev)

                prev = i
                if first == float("inf"):
                    first = i

                last = i

        return min(min_diff, 24*60-last+first)
