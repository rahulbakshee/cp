class Solution:
    def confusingNumber(self, n: int) -> bool:
        num = n
        changed = 0
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        while n:
            rem = n%10
            if rem not in mapping:
                return False

            changed = changed * 10 + mapping[rem]
            n = n//10

        return num != changed
