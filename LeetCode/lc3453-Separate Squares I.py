# https://leetcode.com/problems/separate-squares-i/solutions/6426091/python-binary-search-with-precision-100-beat/

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def helper(point):
            aabove, abelow = 0,0

            for x,y,l in squares:
                total = l*l

                if point <= y:
                    aabove += total
                elif point >=y+l:
                    abelow += total
                else:
                    aheight = y+l-point
                    bheight = point -y
                    aabove += l * aheight
                    abelow += l* bheight
            return aabove - abelow
                


        low = 0
        high = 10**10
        iterations = 0

        while high-low >= pow(10, -5):
            mid = (low+high)/2

            diff = helper(mid)

            if diff <=0:
                high = mid
            else:
                low = mid

            iterations += 1
        print(iterations)
        return high
