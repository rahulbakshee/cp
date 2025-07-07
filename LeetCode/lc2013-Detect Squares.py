# "add"  - keep adding the upcoming points in a list as well as hashmap. 
# "count" - maintain the freq of the upcoming points in defaultdict. get coordinate(px & py) from query point and try to find another points(x, y) from the hashmap to create a diagonal. diagonal is when abs(px-x) == abs(py-y). Also this hould not be a zero area square meaning px!=x and py!=y. after these checks, multiply frequency of the rest of the two points forming a square. (px,py), (x, y) earlier points, find the ther two points like (px, y) and (x, py) and multiply their frequency and add to result.
# time:O(1) for add, O(n) for count, space:O(n)
from collections import defaultdict
class DetectSquares:
    # space:O(n)
    def __init__(self):
        self.points_hashmap = defaultdict(int) # {point:freq}
        self.points_list = list() # for adding upcoming points

    # time:O(1)
    def add(self, point:List[int])->None:
        self.points_hashmap[tuple(point)] += 1    # REMEMBER to convert into tuple
        self.points_list.append(point)
    
    # time:O(n)
    def count(self, point:List[int])->int:
        result = 0
        px, py = point

        # search in the hashmap for a pair with diagonal
        for x, y in self.points_list:
            if ((abs(x-px) != abs(y-py)) # check for diagonal length between points
                or px==x or py == y) : # check for zero area squares
                continue

            result += self.points_hashmap[(x, py)] * self.points_hashmap[(px, y)]

        return result

            
