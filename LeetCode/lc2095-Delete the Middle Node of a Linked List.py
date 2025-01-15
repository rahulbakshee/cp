# one pass  - fast and slow pointers - time:O(n), space:O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # when fast reaches end(None)
        # delete the slow node
        slow.next = slow.next.next

        return head



# two pass - time:O(n), space:O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        # calculate the total length
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next

        if length == 1:
            return 
        

        # iterate to delete the node
        dummy = ListNode(next=head)
        curr = head
        index_to_be_deleted = length //2
        print("index_to_be_deleted", index_to_be_deleted)
        while curr.next:
            if index_to_be_deleted ==1:
                curr.next = curr.next.next
            else:
                curr = curr.next
            index_to_be_deleted -= 1
            print(index_to_be_deleted)
        return dummy.next
