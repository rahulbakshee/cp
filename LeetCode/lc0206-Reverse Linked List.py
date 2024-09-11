# using stack - time:O(n), space:O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        # add to stack
        stack = []
        while head:
            stack.append(head)
            head = head.next

        # remove from stack
        curr = dummy = ListNode()
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None            

        return dummy.next


# iterative
# O(n), space:O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# recursive
# time:O(n), space:O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return new_head


# recursive - timeO(n), space:O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        # reverse the rest of the linkedlist and put first element at end
        rest = self.reverseList(head.next)

        head.next.next = head

        head.next = None
        return rest
        

