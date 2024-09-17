#########################################
# very good explaination - https://leetcode.com/problems/remove-nodes-from-linked-list/editorial/
##########################################
REVIST the EDITORIAL


#option 3 - reverse twice, time:O(n), space:O(1)
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_linkedlist(head):
            if not head:
                return 
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev


        # reverse the LinkedList
        head = reverse_linkedlist(head)

        prev = None
        curr = head
        prefix = 0
        while curr:
            if curr.next and curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return reverse_linkedlist(head)
