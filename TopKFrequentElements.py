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


# OPTIMMIZED
# TC: T: O(n log k) S: O(n + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        heap = []

        for key, count in freq.items():
            if len(heap) == k:
                heappushpop(heap, (key, count))
            else:
                heappush(heap, (key, count))
        return [item[1] for item in heap]
