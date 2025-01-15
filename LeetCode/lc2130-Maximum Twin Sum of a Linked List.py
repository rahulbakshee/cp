# using a separate list of integers to store ListNode values
# time:O(n), space:O(n)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head

        # keep iterating over LL and keep pushing val to list
        while curr:
            values.append(curr.val)
            curr = curr.next

        # use two pointers to compare items in values list
        maximum = float("-inf")
        left, right = 0, len(values)-1
        while left<right:
            maximum = max(maximum, values[left]+values[right])
            left += 1
            right -= 1

        return maximum



# reverse second half in space
# time:O(n), space:O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the middle in linkedlist
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of linkedlist using slow as the mid point
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # calculate the maximum
        start = head
        maximum = float("-inf")
        while prev:
            maximum = max(maximum, prev.val+start.val)
            prev = prev.next
            start = start.next

        return maximum
