# time:O(n), space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node pointing to head
        dummy = ListNode()
        dummy.next = head
        
        # start iterating from head and swap prev and curr
        prev = dummy
        curr = head
        while curr and curr.next:
            # swap
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr

            # reassign prev and curr
            prev = curr
            curr = curr.next

        # return dummy.next
        return dummy.next
        
        
