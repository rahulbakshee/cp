MUST READ THE EDITORIAL

# time:O(n), space:O(1)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1

        for _ in range(n):
            result.append(curr)
            # if curr*10 is within limits
            if curr * 10 <= n:
                curr = curr*10

            else:
                while curr %10 == 9 or curr >=n:
                    curr = curr // 10
                curr  += 1
            #print(result)
        return result
