# time:O(nlogn), space:O(sorting OR logn)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr) == sorted(target)

# time:O(n), space:O(n)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr) != len(target):
            return False

        target_dict = {}
        arr_dict = {}
        for i in range(len(target)):
            if target[i] not in target_dict:
                target_dict[target[i]] = 1
            else:
                target_dict[target[i]] += 1

            if arr[i] not in arr_dict:
                arr_dict[arr[i]] = 1
            else:
                arr_dict[arr[i]] += 1

        return target_dict == arr_dict

            
