# HEAP / PRIORITY QUEUE
# TC: T: O(n) S: O(log n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
