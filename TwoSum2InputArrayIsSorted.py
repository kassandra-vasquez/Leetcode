# TC: T: O(n) S: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            val = numbers[l] + numbers[r]

            if val > target:
                r -= 1
            elif val < target:
                l += 1
            else:
                return [l+1, r+1]
