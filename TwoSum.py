# BRUTE FORCE
# TC: T: O(n^2) S: O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# OPTIMIZED
# TC: T&S: O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i, j in enumerate(nums):
        diff = target - j
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[j] = i
