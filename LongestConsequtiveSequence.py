# ARRAYS AND HASHING

# BRUTE FORCE
# TC: T: O(n log n) S: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_streak += 1
                else:
                    longest = max(longest, curr_streak)
                    curr_streak = 1
        return max(longest, curr_streak)
