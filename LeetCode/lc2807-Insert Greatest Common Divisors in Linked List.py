# euclid algo for GCD - time:O(n*logm), space:O(1)
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b!= 0:
                a, b = b, a%b
            return a

        # # recursive 
        # def gcd(a,b):
        #     if b ==0:
        #         return a
        #     return gcd(b,a%b)

        if not head or not head.next:
            return head

        curr = head
        while curr and curr.next:
            gcd_val = gcd(curr.val, curr.next.val)
            temp = ListNode(gcd_val)

            # assign pointers
            temp.next = curr.next
            curr.next = temp

            # move curr to next
            curr = curr.next.next
        return head



# LONGER - time:O(n*m) - nis len of LL, m is max val of any node in all the nodes
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gca(a, b):
            max_gca = 1
            for i in range(1, min(a,b)+1):
                if a%i==0 and b%i==0:
                    max_gca = max(max_gca, i)
            return max_gca

        curr = head
        curr.next = head.next
        while curr and curr.next:
            temp_val = gca(curr.val, curr.next.val)
            temp = ListNode(temp_val)

            # pointers
            temp.next = curr.next
            curr.next = temp
            
            # increase the curr 
            curr = curr.next.next

        return head
