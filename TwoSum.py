# BRUTE FORCE
# TC: T: O(n^2) - quadratic/worst S: O(1) - constant/best
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# OPTIMIZED
# TC: T&S: O(n) - linear/fair
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i, j in enumerate(nums):
        diff = target - j
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[j] = i
