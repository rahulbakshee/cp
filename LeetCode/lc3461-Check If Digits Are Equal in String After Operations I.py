# time:O(n), space:O(n)


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        list_s = [int(a) for a in list(s)]
        
        while len(list_s) != 2:
            res = []
            for a, b in zip(list_s, list_s[1:]):
                val = (a+b)%10
                res.append(val)
            list_s = res.copy()
            # print(res)

        return list_s[0] == list_s[1]
