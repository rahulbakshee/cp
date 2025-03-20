# iterative
# time:O(n+m), space:O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        # loop over until one of them is exhausted
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        
        # once either of them is exhausted
        if list1:
            node.next = list1
        if list2:
            node.next = list2
            
        return dummy.next
        


# recursive
# time:O(n+m), space:O(n+m)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(list1, list2):
            # base cases
            if not list1 and not list2:
                return  
            if not list1:
                return list2
            if not list2:
                return list1

            # compare element by element from the two lists
            if list1.val < list2.val:
                node = ListNode(list1.val)
                node.next = recurse(list1.next, list2)
            else:
                node = ListNode(list2.val)
                node.next = recurse(list1, list2.next)


            return node

        return recurse(list1, list2)  
