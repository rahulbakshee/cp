"""monotonic increasing stack to keep track of indices and heights.
If the current bar is lower than the top of the stack, we’ve found 
the right boundary for the top bar.
Pop from the stack, calculate area, and track the max area.
At the end, process remaining bars in the stack — treat the end of 
the histogram as the right boundary."""
# time:O(n), space:O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stack will store [index, height] pairs; 
        # it's monotonic increasing by height

        for i, h in enumerate(heights):
            start = i  # this marks the earliest index where current 
            # height h can extend

            # Pop from stack while the current bar is lower than the 
            # bar at the top of the stack. This means we’ve hit the 
            # right boundary for the taller bars in stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate the area for the popped bar
                max_area = max(max_area, height * (i - index))
                start = index  # update start to extend current bar leftward

            # Push current bar with possibly earlier start (after popping taller bars)
            stack.append([start, h])

        # Final pass: remaining bars in stack extend to the end of the histogram
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
