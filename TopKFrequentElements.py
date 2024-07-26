# BRUTE FORCE
# TC: T: O(n log(n)) - O(n) builds counts hash/O(n log n) sorting hash  S: O(n) - n is number of elements in num
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = []

        for element, freq in counts.items():
            heappush(min_heap, (freq, element))
            if len(min_heap) > k:
                heappop(min_heap)
        return [num for (counts, num) in min_heap]
