"""
Algorithm
Main method insertGreatestCommonDivisors:

If the list contains only one node (head.next is null), return the head 
as no insertion is needed.
Initialize ListNode variables node1 and node2 to head and head.next 
respectively, to traverse the linked list.
While node2 is not null:
    Calculate the GCD's of the values in node1 and node2.
    Create a new ListNode gcdNode with the calculated GCD value.
    Update node1.next to gcdNode.
    Update gcdNode.next to node2.
    Set node1 to node2 and node2 to node2.next, respectively. This essentially 
    moves node1 and node2 to the next pair of nodes in the list.
Return the modified head of the list as our answer.
Complexity Analysis
Let n be the number of nodes in the linked list.

Time complexity: O(n⋅log(min(a,b)))

The algorithm traverses the list, visiting each node exactly once. 
This takes linear time. The GCD is calculated using the Euclidean algorithm, 
which has a time complexity of O(log(min(a,b))), where a and b are 
numbers whose GCD is being calculated.

Thus, the overall time complexity of the algorithm is O(n⋅log(min(a,b))).

Space complexity: O(1)

The iterative implementation of the GCD method has a space complexity of O(1).

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # recursive way
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        # iterative way
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a

        # iterate over linkedlist two nodes at at time
        # and find gcd. insert a node with that value

        if not head or not head.next:
            return head

        curr = head
        while curr and curr.next:
            val = gcd(curr.val, curr.next.val)
            new_node = ListNode(val)

            # assign pointers
            new_node.next = curr.next
            curr.next = new_node
                        
            curr = curr.next.next        

        return head
