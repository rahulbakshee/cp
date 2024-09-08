class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")
        return str(bin(int(year)))[2:] +"-" + str(bin(int(month)))[2:] +"-" + str(bin(int(day)))[2:]
