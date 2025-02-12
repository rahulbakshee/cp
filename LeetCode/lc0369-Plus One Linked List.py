# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time:O(n), space:O(1)
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        not_nine = dummy

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return dummy if dummy.val else dummy.next
