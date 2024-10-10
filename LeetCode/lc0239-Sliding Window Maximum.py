class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        start = 0
        q = collections.deque()

        for end in range(len(nums)):
            # pop smaller values from queue
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            # append the curr
            q.append(end)

            # remove left val from window
            if start > q[0]:
                q.popleft()

            if end+1 >=k:
                result.append(nums[q[0]])
                start += 1
        return result
