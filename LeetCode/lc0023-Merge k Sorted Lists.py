# 1- bruteforce - sorting  - time:O(nlogn), space:O(n)
# get all values from all the linked lists
# store them in an array/list
# sort them in ASC
# create a new llinkedlist and put the values of listnodes from newly created array
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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


# 2 - Convert merge k lists problem to merge 2 lists (k-1) times. 
# time:O(kn), space:O(1) - k is the numbe of linkedlists, n total number of nodes in two LL
"""
l1, l2, l3, l4, l5
\    /
  l12
   \    /
    l123
      \    /
       l1234
          \     /
            l12345
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
                    list1.next = recurse(list1.next, list2)
                    return list1
                else:
                    list2.next = recurse(list1, list2.next)
                    return list2

            return recurse(list1, list2)  

        result = None
        for i in range(len(lists)):
            result = mergeTwoLists(result, lists[i])

        return result


# 3- merge with divide and conquer
# Pair up k lists and merge each pair.
# After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
# Repeat this procedure until we get the final sorted linked list.
# Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log k base 2 times.
# time:O(nlogk), space:O(1)
"""
l1, l2, l3, l4, l5, l6
\    /   \   /   \  /
  l12     l34     l56
   \      /        /
    l1234        /
      \       /
        l123456

"""
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



########################################
# important thing to rememebr - 

total_len = len(lists)
if total_len == 0:
    return 

interval = 1
while interval < total_len:
    for i in range(0, total_len - interval, interval *2):
        lists[i] = mergeTwoLists(lists[i], lists[i+interval])
    interval *= 2

return lists[0]
