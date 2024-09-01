class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        mapping = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

        if ((mapping[coordinate1[0]]%2 == 1 and int(coordinate1[1])%2 == 1) or
            (mapping[coordinate1[0]]%2 == 0 and int(coordinate1[1])%2 == 0)):
            black1 = True
        else:
            black1 = False
        
        if ((mapping[coordinate2[0]]%2 == 1 and int(coordinate2[1])%2 == 1) or
            (mapping[coordinate2[0]]%2 == 0 and int(coordinate2[1])%2 == 0)):
            black2 = True
        else:
            black2 = False

        print(black1, black2)        
        return black1 == black2
