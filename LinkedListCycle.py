# BRUTE FORCE
# TC: T&S: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        H = {}
        currNode = head

        while currNode is not None:
            if currNode in H:
                return True
            H[currNode] = True
            currNode = currNode.next
        return False


# OPTIMIZED
# TC: T: O(n) S: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
