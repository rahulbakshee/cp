# time:O(nlogn + mlogm), space:O(n+m)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # sort heaters
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("+inf")]

        # sort houses
        houses.sort()

        
        max_distance = 0
        index = 0

        for house in houses:
            while house > heaters[index]:
                index += 1

            left = house - heaters[index-1]
            right = heaters[index] - house
            dist = min(left,right)
            max_distance = max(max_distance, dist)

        return max_distance





# houses = [2,3,1,4]
# heaters = [4,1] - > [1,4]


# 1    4
#    2
# distance = [max(1,2)] -> 2



# 1    4
#    3
# distance = [max(2,1)] -> 2



# 1    4
#    1
# distance = [max(0,3)] -> 3


# 1    4
#    4
# distance = [max(3,0)] -> 3
