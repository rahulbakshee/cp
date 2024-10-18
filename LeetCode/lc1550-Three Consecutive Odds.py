# brute force
# time:O(n), space:O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            count = 0
            for num in arr[i:i+3]:
                if num%2==1:
                    count +=1
                
                if count == 3:
                    return True

        return False

# counting
# time:O(n), space:O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] %2==1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True

        return False


# product
# time:O(n), space:O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            product = arr[i] * arr[i+1] * arr[i+2]
            if product %2 ==1:
                return True

        return False
