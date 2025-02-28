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




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_len = len(lists)

        interval = 1
        while interval < total_len:
            for i in range(0, total_len-interval, interval*2):
                lists[i] = self.merge_pairs(lists[i], lists[i+interval])
            interval *= 2

        return lists[0] if total_len >0 else None


    def merge_pairs(self, list1, list2):
        if not list1 and not list2:
            return 
        if not list1:
            return list2
        if not list2:
            return list1

        # while both are no empty
        # compare them 
        dummy = head = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        # if either of them are non empty
        # append them to the final result
        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return dummy.next
