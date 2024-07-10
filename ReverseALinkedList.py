# BRUTE FORCE
# TC: T: O(2n) S: O(n) - stack + O(n) - linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while (head != None):
            stack.append(head.val)
            head = head.next

        dummy = ListNode()
        ptr = dummy

        while (stack):
            ptr.next = ListNode(stack.pop())
            ptr = ptr.next
        return dummy.next

# OPTIMIZED
# TC: T: O(n) S: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
