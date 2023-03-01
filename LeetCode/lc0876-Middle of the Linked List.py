# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force space:O(1), time:O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Iter = head
        l = 0
        while Iter:
            l += 1
            Iter = Iter.next

        for i in range(l//2):
            head = head.next
        return head


# space:O(n), time:O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Iter = head
        l = 0
        result = []
        while Iter:
            l += 1
            result.append(Iter)
            Iter = Iter.next

        return result[len(result)//2]

        
# two pointers space:O(1), time:O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow