class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]
                if curr_sum%2:
                    result += 1

        MOD = 10**9+7
        return result%MOD


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = prefix = 0
        MOD = 10**9+7

        odds = 0
        evens = 1

        for num in arr:
            prefix += num

            if prefix%2 == 0:
                evens += 1
                result += odds
            else:
                odds += 1
                result += evens

            result %= MOD

        return result%MOD
