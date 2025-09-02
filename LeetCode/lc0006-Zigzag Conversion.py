class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [""] * numRows
        index, back = 0,True

        for char in s:
            result[index] += char

            if index == 0 or index == numRows -1:
                back = not back

            if back:
                index -= 1
            else:
                index += 1


        return "".join(result)
