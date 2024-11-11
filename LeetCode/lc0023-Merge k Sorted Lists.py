class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1- bruteforce - sorting  - time:O(nlogn), space:O(n)
        # get all values from all the linked lists
        # store them in an array/list
        # sort them in ASC
        # create a new llinkedlist and put the values of listnodes from newly created array

        all_nodes = []
        for l in lists:
            while l:
                all_nodes.append(l.val)
                l = l.next

        # sorting
        all_nodes.sort()

        # craete a new LL
        dummy = curr = ListNode(-1)
        for node in all_nodes:
            curr.next = ListNode(node)
            curr = curr.next

        return dummy.next
