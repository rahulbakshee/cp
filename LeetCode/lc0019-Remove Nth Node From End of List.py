# two pass - one pass to calculate the length of linkedlist and second to access the node before the node-to-be-dropped

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        print(length)

      
        curr = dummy = ListNode(0)
        dummy.next = head
        while length > n:
            curr = curr.next
            length -= 1
        
        curr.next = curr.next.next
        return dummy.next
        


# tow pointers
# time:O(n), space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head
        while n>0 and right:
            n -= 1
            right = right.next

        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
