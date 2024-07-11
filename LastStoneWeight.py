# BRUTE FORCE
# TC: T: O(n^2 log n) S: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest1 = stones.pop()
            heaviest2 = stones.pop()
            if heaviest1 != heaviest2:
                stones.append(abs(heaviest1 - heaviest2))
        return stones[0] if stones else 0


# OPTIMIZED
# TC: T: O(n log n) S: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
