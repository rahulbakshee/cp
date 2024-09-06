# https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview/

# using division operator - when there is no zeros in nums. time-O(n), space-O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        for i in nums:
            prod *= i
    
        for i in nums:
            result.append(int(prod//i))
    
        return result



# using two loops- time-O(n**2), space-O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [None] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            print(i)
            answer[i] = prod

        return answer

# using two separate arrays.time O(n), space O(n)
def getProduct(nums:list)->list:
    result = []
    pre = [1]*len(nums)
    suff = [1]*len(nums)

    for i in range(len(nums)):
        if i ==0:
            pre[i] = 1
        else:
            pre[i] = pre[i-1] * nums[i-1]  

    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            suff[i] = 1
        else:
            suff[i] = suff[i+1] * nums[i+1]

    for i in range(len(nums)):
        result.append(pre[i] * suff[i])

    return result


# using single result array to store and update products - time O(n), space O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
               
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref = pref * nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post = post * nums[i]

        return res
