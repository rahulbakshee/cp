# time:O(n), space:O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -=1

        return True


# time:O(n), space:O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # find middle (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check for palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left  = left.next
            right = right.next


        return True
